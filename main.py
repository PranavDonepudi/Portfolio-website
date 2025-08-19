from flask import Flask, render_template, request
from replit import db
import requests
import datetime

app = Flask('app')

db['projects'] = ["https://replit.com/@triptych/My-RPG-Persona?v=1", "https://replit.com/@triptych/Etch-A-Scape?v=1", "https://replit.com/@triptych/Space-Race?v=1", "https://replit.com/@triptych/Time-For-Cats?v=1", "https://replit.com/@triptych/Pixel-Doodle-Svelte?v=1"]

username = "triptych"

query = """query userByUsername($username: String!) {
    userByUsername(username: $username) {
      fullName
      bio
      image
  }
}"""

repl_query = """query repl($url: String!) { repl(url: $url) { ...on Repl { 
  title url id timeCreated lastPublishedAt language rootOriginReplUrl size description commentCount likeCount publicForkCount runCount config { gitRemoteUrl } } } }"""

def get_data(query, vars):
  return requests.post("https://replit.com/graphql", json={"query":query, "variables":vars}, headers={"Referer": "https://replit.com", "X-Requested-With":"replit", "Cookie": "connect.sid="}).json()

def add_blog(title, desc):
  today = datetime.date.today()

  date = today.strftime("%B %d, %Y")
  
  db["blogs"].append([title, desc, date])

add_blog("My life", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed tempus urna et pharetra pharetra massa massa ultricies. Id aliquet lectus proin nibh nisl. Euismod lacinia at quis risus sed vulputate. Consectetur adipiscing elit ut aliquam purus sit. Fusce ut placerat orci nulla. Fringilla phasellus faucibus scelerisque eleifend. Vitae auctor eu augue ut lectus arcu. Lacus luctus accumsan tortor posuere. Feugiat nibh sed pulvinar proin gravida hendrerit. Fermentum et sollicitudin ac orci phasellus egestas. Consequat id porta nibh venenatis cras sed felis. Suspendisse sed nisi lacus sed. Adipiscing elit ut aliquam purus. Sed arcu non odio euismod lacinia. Sapien et ligula ullamcorper malesuada proin libero nunc consequat. Cursus metus aliquam eleifend mi in nulla posuere. Eget nulla facilisi etiam dignissim diam quis enim. Dui vivamus arcu felis bibendum ut. Integer enim neque volutpat ac tincidunt.")

@app.route('/')
def profile():
  if request.host.endswith('id.repl.co'):
    return 'Open this in a new tab for better results'
    
  name=get_data(query, {"username":"triptych"})['data']['userByUsername']['fullName']
  
  bio=get_data(query, {"username":username})['data']['userByUsername']['bio']
  
  image=get_data(query, {"username":username})['data']['userByUsername']['image']

  all_projects = db['projects']
  
  projects = []

  for project_url in all_projects:
    repl_data = get_data(repl_query, {"url":project_url})

    title = repl_data['data']['repl']['title']
    desc = repl_data['data']['repl']['description']

    likes = repl_data['data']['repl']['likeCount']
    comments = repl_data['data']['repl']['commentCount']
    runs = repl_data['data']['repl']['runCount']

    project = [title, desc, likes, comments, runs, project_url]

    projects.append(project)

  return render_template('profile.html', username=username, name=name, bio=bio, image=image, projects=projects)

@app.route('/blog')
def blog():
  image=get_data(query, {"username":username})['data']['userByUsername']['image']
  
  blogs = db['blogs']

  shortened_blogs = []

  for blog in blogs:
    shortened_blogs.append(blog)

  for index, shortened_blog in enumerate(shortened_blogs):
    if len(shortened_blog[1]) > 520:
      print(shortened_blogs[index][1])
      shortened_blogs[index][1] = shortened_blog[1].replace(shortened_blog[1][-(len(shortened_blog[1])-520):], '...')
  
  return render_template('blogs.html', username=username, blogs=shortened_blogs, image=image)

@app.route('/blog/<title>')
def search_blog(title):
  image=get_data(query, {"username":username})['data']['userByUsername']['image']
  
  blogs = db['blogs']

  for blog in blogs:
    if blog[0] == title:
      return render_template('blog.html', username=username, blog=blog, imaeg=image)

app.run(host='0.0.0.0', port=8080)