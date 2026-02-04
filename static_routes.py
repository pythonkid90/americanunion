from flask import Blueprint, send_from_directory

static = Blueprint('static', __name__, template_folder='templates', static_folder='static')

@static.route('/robots.txt')
def robots_txt():
    return send_from_directory(static.static_folder, 'pages/robots.txt')

@static.route('/humans.txt')
def humans_txt():
    return send_from_directory(static.static_folder, 'pages/humans.txt')

@static.route('/dogs.txt')
def dogs_txt():
    return send_from_directory(static.static_folder, 'pages/dogs.txt')