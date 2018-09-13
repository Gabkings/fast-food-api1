from flask import Flask, request
from flask_restful import Resource
from .models import Order, orders


class OrderDetals(Resource):
    

    def get(self, id):
        order = Order().get_order_by_id(id)
        
        if not order:
            return {"message":"Order not found"}, 404

        return {"order": order.collect_order_details()}, 200

        

    def delete(self, id):
        # global orders
        # orders = list(filter(lambda x: x['id'] != id, orders))
        # return {"messsage": "item deleted"}
        order = Order().get_order_by_id(id)

        if not order:
            return {"message":"Order not found"}, 404
            orders.remove(order)
        return {"message":"order deleted successfully"},200
        

    def put(self, id):
        # data = request.get_json()
        order = Order().get_by_id(id)

        if order:
            return {"message":"Order not found"}, 404
            order.status="approved"
        return {"message":"status approved"}
        

class NewOrderPlacement(Resource):

    def post(self):
        data = request.get_json()
        order = Order(data['name'], data["price"],data['no_of_items_ordered'])
        orders.append(order)

        return {"message":"Food order created"}, 201



class DisplayAllOrders(Resource):
    def get(self):
        return {"orders":[order.collect_order_details() for order in orders]}
        