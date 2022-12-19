MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
'''a variável is_on serve para controlar quando o código tem que parar de executar'''


def is_resource_sufficient(order_ingredients):
    '''a função verifica se há ingredientes suficientes, para isso, ela usa um for loop, iterando pelos itens,
     depois, retorna falso se não houver itens ou verdadeiro, se tiver, observar a diferente posição do return
      na identação.'''

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, theres is not enough {item}!")
            return False
    return True


def process_coins():
    '''retorna o total pago de acordo com as moedas inseridas'''
    print("Please, insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

'''retorna True se for aceito ou falso se não for'''
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that is not enough money. Money refunded.")
        return False
"""a função interna round arredonda por dois, nesse caso"""
'''foi necessário declarar o global, pois profit está no escopo global e precisamos usá-lo no local'''

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} . Enjoy!")



is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink_cost["cost"])
            make_coffee(choice, drink["ingredients"])
            '''primeiro a função is_resource_sufficient verifica se tem ingredientes, depois a função
             is_transaction_successful(money_received, drink_cost) passa a ter os parâmetros acima, ou seja,
            o money_received passa a ser o payment que é a função para verificar as moedas, que faz a verificação que foi
            determinada na função, já o drink_cost busca o cost no dicionário. Portanto, primeiro,
            verifica os ingredientes, depois, verifica as moedas depositadas, depois manda fazer o café e diminui dos
            ingredientes'''
