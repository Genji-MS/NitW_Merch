# tests.py
from pymongo import MongoClient
from unittest import TestCase, main as unittest_main, mock
import bson.objectid 
from bson.objectid import ObjectId
from app import app #throws error when reading pymongo unless pymongo is installed in the (env)

client = MongoClient()
db = client.itemlist
itemlist = db.itemlist
cartlist = db.cartlist
cartlist.delete_many({})

class ContractorTests(TestCase):
    """Flask tests."""

    def setUp(self): #Why is override function written in camelCase? 'set Up' isn't the same as 'Setup' to avoid confusion as a setter/getter it should be named 'setup', or 'setup_tests' for clarity
        """Stuff to do before every test"""
        #Get the Flask test client
        self.client = app.test_client()

        #Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Tests the playlist homepage"""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Sketch', result.data)

    def test_store_show_item(self):
        """Test view single store item"""
        selection = itemlist.find_one({'title':'Sketch'})
        itemlist_id = ObjectId.__str__(selection.get("_id"))
        result = self.client.get(f'/store_item/{itemlist_id}')
        #self.assertEqual(b'60.0', id)
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Genius college student', result.data)

    def test_store_purchase(self):
        """Buying an additional item"""
        selection = itemlist.find_one({'title':'Sketch'})
        itemlist_id = ObjectId.__str__(selection.get("_id"))
        result = self.client.get(f'/store_item/{itemlist_id}/purchase')
        self.assertEqual(result.status, '302 FOUND')
        self.assertEqual(cartlist.find_one({'title':'Sketch'})['item_id'],selection['_id'])
        
    def test_cart_delete(self):
        """Test deleting item from cart"""
        #delete everything from cart to begin
        cartlist.delete_many({})
        #find one item, and push it into our cart
        selection = itemlist.find_one({'title':'Sketch'})
        itemlist_id = ObjectId.__str__(selection.get("_id"))
        cartitem = {
            'item_id': selection.get('_id'),
            'title': selection.get('title'),
            'image_sm': selection.get('image_sm'),
            'price': selection.get('price'),
            'quantity':1
        }
        cartlist.insert_one(cartitem).inserted_id
        #get data of the item
        selection = cartlist.find_one({'title':'Sketch'})
        itemlist_id = ObjectId.__str__(selection.get("_id"))
        #test delete, verify a redirect, that our cartlist no longer contains the item, and the cart is empty
        result = self.client.post(f'/store_cart/{itemlist_id}/delete', data = itemlist_id)
        self.assertEqual(result.status, '302 FOUND')
        self.assertIsNone(cartlist.find_one({'title':'Sketch'}))
        self.assertEqual(cartlist.count_documents({}),0)

    def test_cart_puchase(self):
        """Test purchasing items from your cart"""
        result = self.client.get('/store_cart/purchase')
        self.assertEqual(result.status, '200 OK')

if __name__ == '__main__':
     unittest_main()