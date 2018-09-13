orders = []


class Order:

    order_id = 1
    def __init__(self,name,price,no_of_items_ordered, status="Pending"):
        self.name=name
        self.price=price
        self.no_of_items_ordered=description
        self.id=Order.order_id
        self.status=status
        

        Order.order_id += 1

    def collect_order_details(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.no_of_items_ordered,
            status=self.status
        )

    def get_order_by_id(order_id):
        ''' Helper function to user detail by id'''
        for order in orders:
            if order.get("id") == int(order_id):
                return order