from flask import Blueprint, redirect, request
from app.models import db, Pokemon, Item
from app.forms import ItemForm

item_routes = Blueprint("items", __name__)

@item_routes.route("/<int:id>", methods=["POST"])
def add_item(id):
    item = Item.query.get(id)

    if item:
        form = ItemForm()
        form['csrf_token'].data = request.cookies['csrf_token']

        if form.validate_on_submit():
            item["name"] = form.data["name"]
            item["happiness"] = form.data["happiness"]
            item["image_url"] = form.data["image_url"]
            item["price"] = form.data["price"]

            return item.to_dict(), 200
        else: 
            return form.errors

    else:
        return {"Errors": "The item could not be found"}, 404


@item_routes.route("<int:id>", methods=["DELETE"])
def delete_item(id):
    item = Item.query.get(id)

    if item:
        db.session.delete(item)
        db.session.commit()

        return {"Message": "The item was delete sucessfully"}, 200

    else:
        return {"Errors": "The item could not be found"}, 404




    