def classification_function1k(square, metro_distance, center_distance,
                              have_balcony, is_combined_bathroom,
                              is_cosmetic_repair, have_tv):
    h1 = (-14.1149 + 0.7779 * square + 6.0228 * metro_distance
          + 1.0834 * center_distance + 0.1274 * have_balcony +
          13.3276 * is_combined_bathroom + 2.3913 * is_cosmetic_repair
          + 2.5540 * have_tv)
    h2 = (-6.90156 - 0.59865 * square - 1.06584 * metro_distance
          + 0.08257 * center_distance + 1.6334 * have_balcony +
          10.12693 * is_combined_bathroom + 3.33414 * is_cosmetic_repair
          + 0.56405 * have_tv)
    h3 = (-10.6996 + 1.6942 * square - 0.7925 * metro_distance
          - 1.1552 * center_distance - 0.1404 * have_balcony +
          13.9788 * is_combined_bathroom - 1.3515 * is_cosmetic_repair
          + 4.8828 * have_tv)
    max_val = max(h1, h2, h3)
    if max_val == h1:
        return 1
    elif max_val == h2:
        return 2
    else:
        return 3


def classification_function2k(square, metro_distance, center_distance, is_combined_bathroom):
    h1 = (-8.36792 + 0.70770 * square + 5.01859 * metro_distance
          + 2.67310 * center_distance + 3.27061 * is_combined_bathroom)
    h2 = (-1.66387 - 0.83986 * square - 1.14837 * metro_distance
          - 0.47919 * center_distance + 2.20546 * is_combined_bathroom)
    h3 = (-7.35927 + 4.38809 * square - 1.92430 * metro_distance
          - 0.94475 * center_distance + 3.94406 * is_combined_bathroom)
    max_val = max(h1, h2, h3)
    if max_val == h1:
        return 1
    elif max_val == h2:
        return 2
    else:
        return 3


def linear_regression1k(number_of_cluster, square, metro_distance, center_distance,
                        have_dishwasher, have_conditioner, is_euro_repair, is_design_repair,
                        is_combined_bathroom, have_fridge, have_washing_machine,
                        have_shower_cabine, have_room_furniture):
    if number_of_cluster == 1:
        return (12426.57 + 508.22 * square + 6759.87 * have_dishwasher
                + 6865.09 * have_conditioner
                - 0.76 * metro_distance)
    elif number_of_cluster == 2:
        return (11254.76 + 670.93 * square - 1.3 * center_distance
                + 6027.60 * is_euro_repair + 9960.55 * is_design_repair
                + 3394.4 * is_combined_bathroom - 8080.38 * have_fridge
                + 5627.46 * have_washing_machine)
    elif number_of_cluster == 3:
        return (7339.4 + 7896.4 * have_dishwasher + 899.3 * square
                + 7644 * have_shower_cabine - 3 * center_distance
                + 7602.9 * is_design_repair + 13190.8 * is_combined_bathroom
                + 6512.7 * have_conditioner - 10643.7 * have_room_furniture)
    else:
        print('err')


def linear_regression2k(number_of_cluster, square, is_cosmetic_repair,
                        have_kitchen_furniture, have_tv, is_design_repair,
                        have_dishwasher, center_distance, have_conditioner,
                        is_combined_bathroom, metro_distance):
    if number_of_cluster == 1:
        return (16236.1 + 239.28 * square - 4287.62 * is_cosmetic_repair
                + 4138.35 * have_kitchen_furniture + 3452.42 * have_tv)
    elif number_of_cluster == 2:
        return (14546.43 + 17831.24 * is_design_repair + 9563.9 * have_dishwasher
                - 1.43 * center_distance + 6542 * have_conditioner
                + 539.35 * square + 4194.92 * is_combined_bathroom - 1.46 * metro_distance
                - 2637.09 * is_cosmetic_repair)
    elif number_of_cluster == 3:
        return (45586.29 + 23408 * is_design_repair
                + 13069.15 * have_dishwasher)
    else:
        print('err')
