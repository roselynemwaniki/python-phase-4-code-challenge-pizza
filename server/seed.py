#!/usr/bin/env python3

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Delete existing data to avoid duplicates
    print("Deleting data...")
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    # Create restaurants
    print("Creating restaurants...")
    shack = Restaurant(name="Karen's Pizza Shack", address='address1')
    bistro = Restaurant(name="Sanjay's Pizza", address='address2')
    palace = Restaurant(name="Kiki's Pizza", address='address3')
    restaurants = [shack, bistro, palace]
    db.session.add_all(restaurants)

    # Create pizzas
    print("Creating pizzas...")
    cheese = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    california = Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red Peppers, Mustard")
    pizzas = [cheese, pepperoni, california]
    db.session.add_all(pizzas)

    db.session.commit()  # Commit restaurants and pizzas first to generate IDs

    # Create RestaurantPizza
    print("Creating RestaurantPizza entries...")
    restaurant_pizzas = [
        RestaurantPizza(price=8.99, pizza_id=cheese.id, restaurant_id=shack.id),
        RestaurantPizza(price=9.99, pizza_id=pepperoni.id, restaurant_id=bistro.id),
        RestaurantPizza(price=10.99, pizza_id=california.id, restaurant_id=palace.id),
    ]
    db.session.add_all(restaurant_pizzas)
    db.session.commit()

    print("Seeding done!")
