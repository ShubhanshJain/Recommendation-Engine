import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Recommendation.settings'
django.setup()
import pandas as pd
from home.models import *

import csv
csv_file = "flipkart_com-ecommerce_sample.csv"

with open(csv_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            product_name = row['product_name']
            product_image = eval(row['image'])[0]
            description = row['description']
            category = row['product_category_tree'].split('>>')[0].strip('[]"')
            price = row['retail_price']

            print(product_name,
                product_image,
                description,
                category,
                price,
            )

            Product.objects.update_or_create(
                name = product_name,
                defaults={
                "product_image" : product_image,
                "description" : description,
                "category" : category,
                "price" : price
                }
            )
        except Exception as e:
            price(e)

print("Products imported successfully")