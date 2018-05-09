from flask import Blueprint

item_blueprint = Blueprint('item', __name__)


@item_blueprint.route('/itme/<string:name>')
def item_page(name):
    pass


