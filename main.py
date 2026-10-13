from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_post=requests.get('https://api.npoint.io/c6bd7919ce3b6779a0f6')
    blog_data=blog_post.json()
    return render_template("index.html", blog=blog_data)

@app.route('/post/<int:blog_id>')
def post(blog_id):
    blog_post=requests.get('https://api.npoint.io/c6bd7919ce3b6779a0f6')
    blog_data=blog_post.json()
    for i in blog_data:
        if i['id']==blog_id:
            t=i['title']
            sub=i['subtitle']
            bo=i['body']
    return render_template("post.html", Title=t, Post_Body=bo, subtitle=sub )


if __name__ == "__main__":
    app.run(debug=True)
