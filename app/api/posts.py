from lib2to3.pgen2 import token
from flask import jsonify, request, url_for, abort
from flask_login import login_required 
from app import db  
from app.models import Post 
from app.api import bp  
from app.api.auth import token_auth 
from app.api.errors import bad_request 

# Posts Endpoints 
# Create Posts, Get Posts (From a single users), Get All the Posts 
# Update a Post by id 
# DELETE a Post by id

@bp.route('/posts/users/<int:id>', methods=['GET']) 
@token_auth.login_required 
def get_post(id): 
    if token_auth.current_user().id != id: 
        abort(403) 
    post = Post.query.filter_by(user_id=id).first_or_404() 
    data = post.to_collection_dict() 
    return data 


