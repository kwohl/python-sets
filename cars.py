makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"), (7, "Hyundai")
)

models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6), (16, "Rogue", 2)
)

colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

# i[0] = model i[1] = color
available_car_colors = (
  (1, 1), (1, 2), (1, 7),
  (2, 1), (2, 3), (2, 7),
  (3, 2), (3, 3), (3, 7),
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8),
  (6, 2), (6, 6), (6, 7),
  (7, 1), (7, 3), (7, 7),
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7),
  (10, 2), (10, 5), (10, 7),
  (11, 3), (11, 6), (11, 8),
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8),
  (14, 2), (14, 5), (14, 8),
  (15, 1), (15, 4), (15, 7)
)


# set of make id numbers associated with models
model_make_ids = set()
for item in models:
    model_make_ids.add(item[2])

# set of model id numbers associated with colors
color_inventory = set()
for item in available_car_colors:
    color_inventory.add(item[0])


makes_dictionary = dict()

for make in makes:
    if make[0] in model_make_ids:
        makes_dictionary[make[1]] = dict()

for (key, value) in makes_dictionary.items():
    for make in makes:
        if key == make[1]:
            for model in models:
                if model[0] in color_inventory:
                    color_list = list()
                    for av_color in available_car_colors:
                        if model[0] == av_color[0]:
                            for color in colors:
                                if color[0] == av_color[1]:
                                    color_list.append(color[1])
                    if model[2] == make[0]:
                        makes_dictionary[key][model[1]] = color_list
                    color_list = []


for key in makes_dictionary.keys():
    print(f"{key}")
    print(f"----------------")
    for (model_key, color_value) in makes_dictionary[key].items():
            print(f"{model_key} available in {', '.join(color_value)}")
    print()

# makes_dictionary['Toyota']["Prius"] = ["Charcoal", "Brick", "Ivory"]
# helpful to write out format with actual values for reference ^