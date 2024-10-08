from locust import HttpUser, task, between
from random import randint

class WebsiteUser(HttpUser):
    wait_time = between(1,5)
    # viewing products
    @task(2)
    def view_products(self):
        # print('view product')
        collection_id = randint(2,6)
        self.client.get(
            f'/store/products/?collection_id={collection_id}',
              name='/store/products')
        
    # viewing product details
    @task(4)
    def view_product(self):
        # print('view product details')
        product_id = randint(1,1000)
        self.client.get(
            f'/store/products/{product_id}',
                        name='/store/products/:id')

    # Add product to cart
    @task(1)
    def add_to_cart(self):
        # print('Add to cart')
        product_id = randint(1,10)
        self.client.post(
            f'/store/carts/items/',
            name='/store/carts/items',
            json={'product_id':product_id,'quantity':1}
        )

    # life cycle
    def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id']

    @task
    def  say_hello(self):
        self.client.post('/playground/hello/')
        


