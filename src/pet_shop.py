

def get_pet_shop_name(pet_shop_dict):
    return pet_shop_dict["name"]

def get_total_cash(pet_shop_dict):
    return pet_shop_dict["admin"]["total_cash"]

def add_or_remove_cash(pet_shop_dict, sum_of_money):
    pet_shop_dict["admin"]["total_cash"] += sum_of_money

def get_pets_sold(pet_shop_dict):
    return pet_shop_dict["admin"]["pets_sold"]

def increase_pets_sold(pet_shop_dict, number):
    pet_shop_dict["admin"]["pets_sold"] += number


def get_stock_count(pet_shop_dict):
    total = 0
    for element in pet_shop_dict["pets"]:
        total += 1
    return total




def get_pets_by_breed(pet_shop_dict, breed):
    list_names = []
    for pet in pet_shop_dict["pets"]:
        if pet["breed"] == breed:
            list_names.append(pet["name"])
    return list_names


def find_pet_by_name(pet_shop_dict, name):
    for pet in pet_shop_dict["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(pet_shop_dict, name):
    pet_with_name = find_pet_by_name(pet_shop_dict, name)
    pet_shop_dict["pets"].remove(pet_with_name)


def add_pet_to_stock(pet_shop_dict, new_pet_shop_dict):
    pet_shop_dict["pets"].append(new_pet_shop_dict)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, number):
    customer["cash"] -= number

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

