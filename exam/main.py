"""
 Онлайн-платформа для заказа цветов:
 id (уникальный идентификатор цветка)
 name (название цветка)
 description (описание цветка)
 price (цена цветка)
 availability (доступность цветка на складе) 



 Добавление новых записей с указанием всех параметров
 Просмотр списка всех доступных продуктов с их атрибутами.
 Обновление информации о записи в базе данных.
 Удаление записи из базы данных.
 Добавление записи в корзину пользователя.
 Оплата содержимого корзины и получение чека в формате Excel.
 Использовать объектно-ориентированный подход при разработке.
 Использовать базу данных для хранения информации о продуктах.
 Обработать исключения, такие как неверный формат ввода или
отсутствие соединения с базой данных.

"""
import psycopg2
from psycopg2 import OperationalError
from tabulate import tabulate

def connect_to_db():
    try:
        conn = psycopg2.connect(
        host="127.0.0.1",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="postgres"
        )
        return conn
    except OperationalError as e:
        print(f"The error {e} occurred")
        
connection = connect_to_db()

cursor = connection.cursor()
class Cart():
        def __init__(self):
            self.order_availability = True
            self.products = set()
            self.price = 0
        def add_product(self, other_product):
            self.check_quantity(other_product)
            if self.order_availability ==  True:
                self.products.add(other_product)
            elif other_product in self.products:
                print('The product you want to add to your cart is already in the cart')  
            else:
                print('There is no product that you want to buy at the moment!')
        def check_quantity(self, other_product):
            query = f'SELECT quantity FROM flower_market WHERE `name`={other_product}'
            cursor.execute(query)
            d = cursor.fetchone()
            if d==0:
                self.order_availability=False
        def remove_product(self, other_product):
            try:
                self.products.remove(other_product.id)
                self.price -= other_product.price
            except KeyError:
                print("This item is not in your order.")
        def show_cart(self):
            print(self.products)
        def show_price(self):
            for i in range(self.products):
                query = f'SELECT price FROM flower_market WHERE `name`={self.products[i]}'
                cursor.execute(query)
                price += cursor.fetchone()        
while True:
    def show_check_price():
        cart.show_price()
    def add_product_in_database():
        name = input()
        description = input()
        price = int(input())
        quantity = int(input())
        query = f"insert into flower_market (name,price,quantity,description) values('{name}',{price}, {quantity}, '{description}')"
        cursor.execute(query)
        connection.commit()
    def show_products():
        query = f"SELECT id FROM flower_market"
        cursor.execute(query)
        id = cursor.fetchall()
        query = f"SELECT name FROM flower_market"
        cursor.execute(query)
        name = cursor.fetchall()
        query = f"SELECT price FROM flower_market"
        cursor.execute(query)
        price = cursor.fetchall()
        query = f"SELECT quantity FROM flower_market"
        cursor.execute(query)
        quantity = cursor.fetchall()
        query = f"SELECT description FROM flower_market"
        cursor.execute(query)
        description = cursor.fetchall()

        for i in id:
            table = tabulate({"id": [f'{i}']}, headers="keys", tablefmt="grid")
        print(table)
    def remove_product_database():
        id = int(input("Enter id to delete: "))
        query = f'delete from flower_market where "id"={id}'
        cursor.execute(query)
        connection.commit()
    def  update_database():
        id = int(input("Enter id to update: "))
        name = input()
        description = input()
        price = int(input())
        quantity = int(input())
        query = f"update flower_market set description='{description}', name='{name}', price={price}, quantity='{quantity}' where " + f'"id"={id}'
        cursor.execute(query)
        connection.commit()
    # def add_to_cart():
    #     print('Hello, choose something you would like to order:')
    #     product_name = input('Write what product you want to add to your cart: ')
    #     global cart
    #     cart = Cart()
    #     if product_name in name:
    #         cart.add_product(product_name)
    print('1. Add new product\n 2. See all products \n 3. Update information in database\n 4. Remove product from database \n 5. Add product in cart\n 6. Pay for my cart')
    admin_choice = int(input())
    match(admin_choice):
        case 1:
            add_product_in_database()
        case 2:
            show_products()
        case 3:
            update_database()
        case 4:
            remove_product_database()
        case 5:
            add_to_cart()
        case 6:
            show_check_price()
            
    
    
    