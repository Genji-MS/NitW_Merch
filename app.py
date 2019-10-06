# app.py
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.itemlist
itemlist = db.itemlist
#Initialize the cartlist DB, The user will be able to modify these entries.
cartlist = db.cartlist
#CHEAP FIX: initialize the cartlist as empty for each session
cartlist.delete_many({})
#Initialize the itemlist DB, The user will not have access to modify these entries.
#KNOWN ISSUE: Because the itemlist DB _id's are dynamic, they will change every restart of the app by doing the below
#This means that they will be 'random' in the cartlist, and not found, when trying to add quantity to an item
itemlist.delete_many({})
itemlist.insert_many([
    {'title':'Draven Blacktalon', 'desc_sm':'Naive, Nerdy, yet Kind.','desc_full':'Adult raven. Big dreamer who moved country to be with whom he thought would be his true love. Starving artist.','image_sm':'store_item_000_s.png', 'image_lg':'store_item_000_l.png', 'price':40.00},
    {'title':'Ally Felli', 'desc_sm': 'Sad, Hot headed, and Stubborn.','desc_full':'Adult cat. Dreams of marriage and children. College drop out.','image_sm':'store_item_001_s.png', 'image_lg':'store_item_001_l.png', 'price':40.00},
    {'title':'Faye Luscus', 'desc_sm':'Naive, Kind, yet Bossy.','desc_full': 'Young adult mouse. Struggling college student. Lives with demanding boyfriend.','image_sm':'store_item_002_s.png', 'image_lg':'store_item_002_l.png', 'price':50.00},
    {'title':'Sketch', 'desc_sm':'Loner. Intelligent, and Creative','desc_full':'Adult bobcat. Genius college student. Moves around a lot.','image_sm':'store_item_003_s.png', 'image_lg':'store_item_003_l.png', 'price':60.00},
    {'title':'Zethany Gomor', 'desc_sm':'Artistic, Intelligent, yet Emotional.','desc_full':'Young adult rabbit. Starving artist and college student. Lives with younger sister whom she supports independently.','image_sm':'store_item_004_s.png', 'image_lg':'store_item_004_l.png', 'price':60.00},
    {'title':'Namrah Gomor', 'desc_sm':'Creative, Loner, and Soft spoken.','desc_full':'Teenage rabbit. Lonely high school student.','image_sm':'store_item_005_s.png', 'image_lg':'store_item_005_l.png', 'price':50.00},
    {'title':'Tamizel Bezella', 'desc_sm':'Creative, Diva, and Bold.','desc_full':'Young adult goat. High school drop out. Moved states to marry and start a family with long distance boyfriend.','image_sm':'store_item_006_s.png', 'image_lg':'store_item_006_l.png', 'price':50.00},
    {'title':'Sam Sun', 'desc_sm':'Jaded, Stubborn, yet Thoughtful.','desc_full':'Young adult dog. Gothic struggling artist with lots of pets.','image_sm':'store_item_007_s.png', 'image_lg':'store_item_007_l.png', 'price':50.00},
    {'title':'James Laurens', 'desc_sm':'Kind, Caring, and Quirky.','desc_full':'Teenage bat. Hopeless romantic high school student.','image_sm':'store_item_008_s.png', 'image_lg':'store_item_008_l.png', 'price':40.00}
])

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage"""
    return render_template('index.html', itemlist = itemlist.find(), cart=cartlist.count() )

@app.route('/store_item/<itemlist_id>', methods=['GET'])
def store_show_item(itemlist_id):
    """View single store item"""
    item = itemlist.find_one({'_id': ObjectId(itemlist_id)})
    return render_template('store_item.html', itemlist=item, cart=cartlist.count() )

@app.route('/store_item/<itemlist_id>/purchase', methods=['GET'])
def store_purchase(itemlist_id):
    """Add item to cart and return to index page"""
    item = itemlist.find_one({'_id': ObjectId(itemlist_id)})
    cartitem = cartlist.find_one({'item_id': ObjectId(itemlist_id)})
    #print (cartitem)
    if cartitem is None:
        cartitem = {
            'item_id': item.get('_id'),
            'title': item.get('title'),
            'image_sm': item.get('image_sm'),
            'price': item.get('price'),
            'quantity':1
        }
        cartlist.insert_one(cartitem).inserted_id
    else:
        #print (f' quantity before{cartitem["quantity"]} ')
        cartitem['quantity'] += 1
        #print (f' quantity after {cartitem["quantity"]} ')
        cartlist.update_one(
            #Looking for the item title is possible to avoid the bug with making a new DB. However not a REAL solution
            {"_id":ObjectId(cartitem["_id"])},
            {'$set':cartitem}
        )
    #√: attempt to find the item in the db, and if true, increase the quantity
    #√: add the item into our cart DB if false
    return redirect(url_for('index'))#, itemlist=itemlist.find(), msg="One item added to Cart"))

@app.route('/store_cart')#Note to self, everything is in templates, stop trying to call /templates/
def cart_view_all():
    """View all items in users cart"""
    total = 0
    for item in cartlist.find():
        total += int(item['price']) * int(item['quantity'])
    print(f' Total: {total}')
    return render_template('store_cart.html', itemlist=itemlist, cart=cartlist.count(), cartlist=cartlist.find(), total = total)

@app.route('/store_cart/<cartitem_id>/delete', methods=['POST'])
def cart_delete(cartitem_id):
    """Delete specified item from cart"""
    cartlist.delete_one({'_id':ObjectId(cartitem_id)})
    return redirect(url_for('cart_view_all'))

@app.route('/store_cart/purchase')
def cart_purchase():
    """Display an exit image, and clear the cart"""
    cartlist.delete_many({})
    return render_template('store_purchase.html', cart = 0)

if app.name == '__main__':
    app.run(debug=True)