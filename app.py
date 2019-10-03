# app.py
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

itemlist = [
    {'title':'Draven Blacktalon', 'desc_sm':'Naive, Nerdy, yet Kind.','desc_full':'Adult raven. Big dreamer who moved country to be with whom he thought would be his true love. Starving artist. Naive, Nerdy, yet Kind.','image_sm':'store_item_000_s.png', 'image_lg':'store_item_000_l.png'},
    {'title':'Ally Felli', 'desc_sm': 'Sad, Hot headed, and Stubborn.','desc_full':'Adult cat. Dreams of marriage and children. College drop out. Sad, Hot headed, and Stubborn.','image_sm':'store_item_001_s.png', 'image_lg':'store_item_001_l.png'},
    {'title':'Faye Luscus', 'desc_sm':'Naive, Kind, yet Bossy.','desc_full': 'Young adult mouse. Struggling college student. Lives with demanding boyfriend. Naive, Kind, yet Bossy.','image_sm':'store_item_002_s.png', 'image_lg':'store_item_002_l.png'},
    {'title':'Sketch', 'desc_sm':'Loner. Intelligent, and Creative','desc_full':'Adult bobcat. Genius college student. Moves around a lot. Loner. Intelligent, and Creative.','image_sm':'store_item_003_s.png', 'image_lg':'store_item_003_l.png'},
    {'title':'Zethany Gomor', 'desc_sm':'Artistic, Intelligent, yet Emotional.','desc_full':'Young adult rabbit. Starving artist and college student. Lives with younger sister whom she supports independently. Artistic, Intelligent, yet Emotional.','image_sm':'store_item_004_s.png', 'image_lg':'store_item_004_l.png'},
    {'title':'Namrah Gomor', 'desc_sm':'Creative, Loner, and Soft spoken.','desc_full':'Teenage rabbit. Lonely high school student. Creative, Loner, and Soft spoken.','image_sm':'store_item_005_s.png', 'image_lg':'store_item_005_l.png'},
    {'title':'Tamizel Bezella', 'desc_sm':'Creative, Diva, and Bold.','desc_full':'Young adult goat. High school drop out. Moved states to marry and start a family with long distance boyfriend. Creative, Diva, and Bold.','image_sm':'store_item_006_s.png', 'image_lg':'store_item_006_l.png'},
    {'title':'Sam Sun', 'desc_sm':'Jaded, Stubborn, yet Thoughtful.','desc_full':'Young adult dog. Gothic struggling artist with lots of pets. Jaded, Stubborn, yet Thoughtful.','image_sm':'store_item_007_s.png', 'image_lg':'store_item_007_l.png'},
    {'title':'James Laurens', 'desc_sm':'Kind, Caring, and Quirky.','desc_full':'Teenage bat. Hopeless romantic high school student. Kind, Caring, and Quirky.','image_sm':'store_item_008_s.png', 'image_lg':'store_item_008_l.png'}
]

@app.route('/')
def index():
    """Return homepage"""
    return render_template('index.html', itemlist = itemlist)

#@app.route('/')
def playlist_index():
    """Show store page"""
    return render_template('playlist_index.html', itemlist= itemlist) #itemlist.find())

@app.route('/playlist/new')
def playlist_new():
    """Create New playlist"""
    return render_template('playlist_new.html', itemlist = {}, title = 'New Playlist')

@app.route('/playlist', methods=['POST'])
def playlist_submit():
    """Submit a new playlist"""
    p_list= { 
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    #Youtube doesn't like to display in this way, replace this component of the URL to embed/ and it'll work fine.
    for index in range(len(p_list['videos'])):
        p_list['videos'][index] = p_list['videos'][index].replace("watch?v=", "embed/")

    #playlist_id = itemlist.insert_one(p_list).inserted_id
    #print(request.form.to_dict())
    #return redirect(url_for('playlist_index'))
    #return redirect(url_for('playlist_show', itemlist_id = itemlist_id))

@app.route('/playlist/<playlist_id>')
def playlist_show(itemlist_id):
    """Show a single playlist"""
    #p_list = itemlist.find_one({'_id': ObjectId(itemlist_id)})
    #p_list_comments = comments.find({'itemlist_id': ObjectId(itemlist_id)})
    #Double check URL's that may have been saved without /embed/ and check that they even have links.
    #if p_list.get('videos'):
    #    for index in range(len(p_list['videos'])):
    #        p_list['videos'][index] = p_list['videos'][index].replace("watch?v=", "embed/")
    #return render_template('playlist_show.html',itemlist=p_list,comments=p_list_comments)

@app.route('/playlist/<playlist_id>/edit')
def playlist_edit(itemlist_id):
    """Show the edit form for a playlist"""
    #p_list = itemlist.find_one({'_id': ObjectId(itemlist_id)})
    #return render_template('playlist_edit.html',itemlist=p_list, title='Edit Playlist')

@app.route('/playlist/<playlist_id>', methods=['POST'])
def playlist_update(itemlist_id):
    """Submit and edited playlist"""
    updated_playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    #Youtube doesn't like to display with watch?, replace this component of the URL to embed/ and it'll work fine.
    for index in range(len(updated_playlist['videos'])):
        updated_playlist['videos'][index] = updated_playlist['videos'][index].replace("watch?v=", "embed/")
    #itemlist.update_one(
        #{'_id':ObjectId(itemlist_id)},
        #{'$set':updated_playlist})
    return redirect(url_for('playlist_show', itemlist_id = itemlist_id))

@app.route('/playlist/<playlist_id>/delete', methods=["POST"])
def playlist_delete(playlist_id):
    """Delete specified playlist"""
    #itemlist.delete_one({'_id': ObjectId(itemlist_id)})
    return redirect(url_for('itemlist_index'))

if app.name == '__main__':
    app.run(debug=True)
    #app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))