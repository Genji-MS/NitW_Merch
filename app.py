# app.py
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

itemlist = [
    {'title':'Draven Blacktalon', 'desc-sm':'Naive, Nerdy, yet Kind.',
    'desc-full':'Adult raven. Big dreamer who moved country to be with whom he thought would be his true love. Starving artist. Naive, Nerdy, yet Kind.',
    'image-sm':'store_item_000_s.png', 'image-lg':'store_item_000_l.png'},
    {'title':'Ally Felli', 'desc-sm': 'Sad, Hot headed, and Stubborn.',
    'desc-full':'Adult cat. Dreams of marriage and children. College drop out. Sad, Hot headed, and Stubborn.',
    'image-sm':'store_item_001_s.png', 'image-lg':'store_item_001_l.png'},
    {'title':'Faye Luscus', 'desc-sm':'Naive, Kind, yet Bossy.',
    'desc-full': 'Young adult mouse. Struggling college student. Lives with demanding boyfriend. Naive, Kind, yet Bossy.',
    'image-sm':'store_item_002_s.png', 'image-lg':'store_item_002_l.png'},
    {'title':'Sketch', 'desc-sm':'Loner. Intelligent, and Creative',
    'desc-full':'Adult bobcat. Genius college student. Moves around a lot. Loner. Intelligent, and Creative.',
    'image-sm':'store_item_003_s.png', 'image-lg':'store_item_003_l.png'},
    {'title':'Zethany Gomor', 'desc-sm':'Artistic, Intelligent, yet Emotional.',
    'desc-full':'Young adult rabbit. Starving artist and college student. Lives with younger sister whom she supports independently. Artistic, Intelligent, yet Emotional.',
    'image-sm':'store_item_004_s.png', 'image-lg':'store_item_004_l.png'},
    {'title':'Namrah Gomor', 'desc-sm':'Creative, Loner, and Soft spoken.',
    'desc-full':'Teenage rabbit. Lonely high school student. Creative, Loner, and Soft spoken.',
    'image-sm':'store_item_005_s.png', 'image-lg':'store_item_005_l.png'},
    {'title':'Tamizel Bezella', 'desc-sm':'Creative, Diva, and Bold.',
    'desc-full':'Young adult goat. High school drop out. Moved states to marry and start a family with long distance boyfriend. Creative, Diva, and Bold.',
    'image-sm':'store_item_006_s.png', 'image-lg':'store_item_006_l.png'},
    {'title':'Sam Sun', 'desc-sm':'Jaded, Stubborn, yet Thoughtful.',
    'desc-full':'Young adult dog. Gothic struggling artist with lots of pets. Jaded, Stubborn, yet Thoughtful.',
    'image-sm':'store_item_007_s.png', 'image-lg':'store_item_007_l.png'},
    {'title':'James Laurens', 'desc-sm':'Kind, Caring, and Quirky.',
    'desc-full':'Teenage bat. Hopeless romantic high school student. Kind, Caring, and Quirky.',
    'image-sm':'store_item_008_s.png', 'image-lg':'store_item_008_l.png'}
]

@app.route('/')
def index():
    """Return homepage"""
    return render_template('index.html', msg='flask flask baby~')

if app.name == '__main__':
    app.run(debug=True)