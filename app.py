# app.py
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.itemlist
itemlist = db.itemlist
itemlist.delete_many({})
itemlist.insert_many([
    {'title':'Draven Blacktalon', 'desc_sm':'Naive, Nerdy, yet Kind.','desc_full':'Adult raven. Big dreamer who moved country to be with whom he thought would be his true love. Starving artist. Naive, Nerdy, yet Kind.','image_sm':'store_item_000_s.png', 'image_lg':'store_item_000_l.png'},
    {'title':'Ally Felli', 'desc_sm': 'Sad, Hot headed, and Stubborn.','desc_full':'Adult cat. Dreams of marriage and children. College drop out. Sad, Hot headed, and Stubborn.','image_sm':'store_item_001_s.png', 'image_lg':'store_item_001_l.png'},
    {'title':'Faye Luscus', 'desc_sm':'Naive, Kind, yet Bossy.','desc_full': 'Young adult mouse. Struggling college student. Lives with demanding boyfriend. Naive, Kind, yet Bossy.','image_sm':'store_item_002_s.png', 'image_lg':'store_item_002_l.png'},
    {'title':'Sketch', 'desc_sm':'Loner. Intelligent, and Creative','desc_full':'Adult bobcat. Genius college student. Moves around a lot. Loner. Intelligent, and Creative.','image_sm':'store_item_003_s.png', 'image_lg':'store_item_003_l.png'},
    {'title':'Zethany Gomor', 'desc_sm':'Artistic, Intelligent, yet Emotional.','desc_full':'Young adult rabbit. Starving artist and college student. Lives with younger sister whom she supports independently. Artistic, Intelligent, yet Emotional.','image_sm':'store_item_004_s.png', 'image_lg':'store_item_004_l.png'},
    {'title':'Namrah Gomor', 'desc_sm':'Creative, Loner, and Soft spoken.','desc_full':'Teenage rabbit. Lonely high school student. Creative, Loner, and Soft spoken.','image_sm':'store_item_005_s.png', 'image_lg':'store_item_005_l.png'},
    {'title':'Tamizel Bezella', 'desc_sm':'Creative, Diva, and Bold.','desc_full':'Young adult goat. High school drop out. Moved states to marry and start a family with long distance boyfriend. Creative, Diva, and Bold.','image_sm':'store_item_006_s.png', 'image_lg':'store_item_006_l.png'},
    {'title':'Sam Sun', 'desc_sm':'Jaded, Stubborn, yet Thoughtful.','desc_full':'Young adult dog. Gothic struggling artist with lots of pets. Jaded, Stubborn, yet Thoughtful.','image_sm':'store_item_007_s.png', 'image_lg':'store_item_007_l.png'},
    {'title':'James Laurens', 'desc_sm':'Kind, Caring, and Quirky.','desc_full':'Teenage bat. Hopeless romantic high school student. Kind, Caring, and Quirky.','image_sm':'store_item_008_s.png', 'image_lg':'store_item_008_l.png'}
])

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage"""
    return render_template('index.html', itemlist = itemlist.find(), msg = "")

@app.route('/store_item/<itemlist_id>', methods=['GET'])
def store_item_read(itemlist_id):
    """View single store item"""
    item = itemlist.find_one({'_id': ObjectId(itemlist_id)})
    return render_template('store_item.html', itemlist = item)

if app.name == '__main__':
    app.run(debug=True)