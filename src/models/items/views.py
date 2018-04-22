from flask import Blueprint

item_blueprint = Blueprint('item', __name__)


@item_blueprint.route('/itme/<string:name>')
def item_page(name):
    pass


@item_blueprint.route('/load')
def load_item():
    '''
    Loads an items data using their store and return a JSON file
    :return:
    '''