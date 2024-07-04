from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.post import Post
from flask_app import app

@app.route("/create_post", methods=['post'])
def create_post():
    if not Post.validate_post(request.form):
        return redirect("/dashboard")
    Post.save(request.form)
    return redirect("/dashboard")

@app.route("/delete/<int:id>")
def delete(id):
    dicc = {'id': id}
    Post.delete(dicc)
    return redirect("/dashboard")