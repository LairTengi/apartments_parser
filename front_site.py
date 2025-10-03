import streamlit as st
import calculations

st.title("Калькулятор расчёта цены аренды квартиры")

count_of_rooms = st.radio(
    "Количество комнат",
    options=[1, 2],
    index=0  # Выбор по умолчанию
)

square = st.number_input(
    "Площадь квартиры (м.кв.)",
    min_value=20.0,
    max_value=100.0,
    step=0.1
)

center_distance = st.number_input(
    "Расстояние до центра (м.)",
    min_value=100,
    max_value=15000,
    step=50
)

metro_distance = st.number_input(
    "Расстояние до ближайшей станции метро (м.)",
    min_value=100,
    max_value=15000,
    step=50
)

type_of_balcony = st.radio(
    "Наличие балкона",
    options=['Балкон', 'Лоджия', 'Отсутствует'],
    index=0  # Выбор по умолчанию
)

type_of_bathroom = st.radio(
    "Тип санузла",
    options=['Совмещённый санузел', 'Раздельный санузел'],
    index=0  # Выбор по умолчанию
)

type_of_repair = st.radio(
    "Тип ремонта",
    options=['Косметический ремонт', 'Евроремонт', 'Дизайнерский ремонт', 'Нет ремонта'],
    index=0  # Выбор по умолчанию
)

type_of_tv = st.radio(
    "Наличие телевизора",
    options=['Да', 'Нет'],
    index=0  # Выбор по умолчанию
)

type_of_fridge = st.radio(
    "Наличие холодильника",
    options=['Да', 'Нет'],
    index=0  # Выбор по умолчанию
)

type_of_washing_machine = st.radio(
    "Наличие стиральной машины",
    options=['Да', 'Нет'],
    index=0  # Выбор по умолчанию
)

type_of_shower = st.radio(
    "Тип ванной комнаты:",
    options=['Ванна', 'Душевая кабина'],
    index=0  # Выбор по умолчанию
)

type_of_kitchen_furniture = st.radio(
    "Наличие кухонной мебели",
    options=['Да', 'Нет'],
    index=0  # Выбор по умолчанию
)

type_of_room_furniture = st.radio(
    "Наличие мебели в комнатах",
    options=['Да', 'Нет'],
    index=0  # Выбор по умолчанию
)

type_of_dishwasher = st.radio(
    "Наличие посудомоечной машины",
    options=['Да', 'Нет'],
    index=1  # Выбор по умолчанию
)

type_of_conditioner = st.radio(
    "Наличие кондиционера",
    options=['Да', 'Нет'],
    index=1  # Выбор по умолчанию
)

if st.button("Рассчитать"):
    square_standardized = (square - 38.4499) / 7.624
    center_distance_standardized = (center_distance - 5175.079) / 2647.553
    metro_distance_standardized = (metro_distance - 2800.111) / 2251.2755

    have_dishwasher = 1 if type_of_dishwasher == 'Да' else 0
    have_conditioner = 1 if type_of_conditioner == 'Да' else 0
    is_euro_repair = 1 if type_of_repair == 'Евроремонт' else 0
    is_design_repair = 1 if type_of_repair == 'Дизайнерский ремонт' else 0
    is_cosmetic_repair = 1 if type_of_repair == 'Косметический ремонт' else 0
    is_combined_bathroom = 1 if type_of_bathroom == 'Совмещённый санузел' else 0
    have_fridge = 1 if type_of_fridge == 'Да' else 0
    have_washing_machine = 1 if type_of_washing_machine == 'Да' else 0
    have_shower_cabine = 1 if type_of_shower == 'Душевая кабина' else 0
    have_balcony = 1 if type_of_balcony == 'Балкон' else 0
    have_tv = 1 if type_of_tv == 'Да' else 0
    have_kitchen_furniture = 1 if type_of_kitchen_furniture == 'Да' else 0
    have_room_furniture = 1 if type_of_room_furniture == 'Да' else 0    

    if count_of_rooms == 1:
        number_of_cluster = calculations.classification_function1k(square_standardized, metro_distance_standardized,
                                                                   center_distance_standardized,
                                                                   have_balcony, is_combined_bathroom,
                                                                   is_cosmetic_repair, have_tv)
        result = calculations.linear_regression1k(number_of_cluster, square, metro_distance, center_distance,
                                                  have_dishwasher, have_conditioner, is_euro_repair, is_design_repair,
                                                  is_combined_bathroom, have_fridge, have_washing_machine,
                                                  have_shower_cabine, have_room_furniture)
        st.success(f"Номер кластера: {number_of_cluster}, Цена аренды квартиры: {round(result, 2)}")
    if count_of_rooms == 2:
        number_of_cluster = calculations.classification_function2k(square_standardized, metro_distance_standardized,
                                                                   center_distance_standardized,
                                                                   is_combined_bathroom)
        result = calculations.linear_regression2k(number_of_cluster, square, is_cosmetic_repair,
                                                  have_kitchen_furniture, have_tv, is_design_repair,
                                                  have_dishwasher, center_distance, have_conditioner,
                                                  is_combined_bathroom, metro_distance)
        st.success(f"Номер кластера: {number_of_cluster}, Цена аренды квартиры: {round(result, 2)}")
