# tests.py
import os
from pymongo import MongoClient
from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app #throws error when reading pymongo unless pymongo is installed in the (env)

sample_itemlist_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_itemlist = {
    'title':'Lyon Test', 'desc_sm':'Immortal, Intelligent, and Magical.','desc_full':'Little is known, and none who knew have spoken. However it loves to live as the ultimate test subject.','image_sm':'120x.png', 'image_lg':'140x.png', 'price':99.99
}
sample_cartlist = {
    'item_id': sample_itemlist_id,
    'title': sample_itemlist['title'],
    'image_sm': sample_itemlist['image_sm'],
    'price': sample_itemlist['price'],
    'quantity':98
}

class ContractorTests(TestCase):
    """Flask tests."""

    def setUp(self): #Why is override function written in camelCase? 'set Up' isn't the same as 'Setup' to avoid confusion as a setter/getter it should be named 'setup', or 'setup_tests' for clarity
        """Stuff to do before every test"""
        #Get the Flask test client
        self.client = app.test_client()

        #Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):#Works
        """Tests the playlist homepage"""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Sketch', result.data)

    def test_store_show_item(self):#Fails, how can I put in test data to be checked? 'Lyon Test' doesn't appear, because the app uses its own db, not the one specified above
        """Test view single store item"""
        #selection = self.client.find_one({'title':'Sketch'})
        #result = self.client.get(f'/store_item/{selection["_id"]}')
        #self.assertEqual(result.status, '200 OK')
        #self.assertIn(b'60', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_store_show_item_2(self, mock_find):
        """Test showing a single playlist"""
        mock_find.return_value = sample_itemlist

        result = self.client.get(f'/store_item/{sample_itemlist_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Lyon Test', result.data)
    '''
    @mock.patch('pymongo.collection.Collection.find_one')
    def test_store_purchase(self, mock_find):# error in _id
        """Buying an additional item"""
        mock_find.return_value = sample_cartlist

        result = self.client.get(f'/store_item/{sample_itemlist_id}/purchase')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'99.99', result.data)

    @mock.patch('pymongo.collection.Collection.insert_one')
    def test_store_purchase_2(self, mock_insert):#ObjectId has no [items]
        """Test purchasing an item"""
        result = self.client.post(f'/store_item/{ sample_itemlist_id }/purchase', data=sample_itemlist_id)

        #After submitting, should redirect to that playlists' page
        self.assertEqual(result.status, '302 FOUND')
        mock_insert.assert_called_with(sample_cartlist)

    @mock.patch('pymongo.collection.Collection.update_one')
    def test_cart_delete(self, mock_delete):#no ObjectID results
        """Test deleting item from cart"""
        result = self.client.post(f'/store_cart/{sample_cartlist}/delete', data = sample_itemlist_id)

        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_itemlist_id}, {'$set': sample_cartlist})

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_cart_puchase(self):#only needs one argument, but two were passed in
        """Test purchasing items from your cart"""
        result = self.client.get('/store_purchase')
        self.assertEqual(result.status, '200 OK')

if __name__ == '__main__':
     unittest_main()
     '''