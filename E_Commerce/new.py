import pandas as pd

pasta = "E_Commerce/CSV/"

orders = pd.read_csv(pasta + "olist_orders_dataset.csv")
items = pd.read_csv(pasta + "olist_order_items_dataset.csv")
payments = pd.read_csv(pasta + "olist_order_payments_dataset.csv")
reviews = pd.read_csv(pasta + "olist_order_reviews_dataset.csv")
customers = pd.read_csv(pasta + "olist_customers_dataset.csv")
sellers = pd.read_csv(pasta + "olist_sellers_dataset.csv")
products = pd.read_csv(pasta + "olist_products_dataset.csv")
categorias = pd.read_csv(pasta + "product_category_name_translation.csv")

print(orders.head())