from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.comment import Comment
from flask_app import app

@app.route("/create_comment", methods=['post'])
def create_comment():  
    Comment.save_comment(request.form)
    return redirect("/dashboard")