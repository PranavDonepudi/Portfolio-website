# Portfolio Website Template
Hi guys, this is a template on creating your very own portfolio website template, using Replit's very own graphql to get your Replit and repl stats. Its responsive, beautiful, and has a classy style to it. Lets get started!

First of all, to get started, go to line 10 and change the `username` variable to your Replit username. This is one of basic steps to get your website running.

Second of all, open `profile.html` in the folder `templates` and go to line 42. This only displays the text because I made this website for @triptych from a Replit bounty and his bio is short, so be sure to replace all contents in `<p>` with `{{bio}}`.

Lastly, go in your console and type `db['blog'] = []`. This is used to avoid a key error in the database.

## Attaching social links

From line 55 to the bottom is our social links. This includes Twitter, Github, etc. and is where you would typically want to put your social links so others can contact you. Feel free to replace the `svg` and links to make them your own.

## Changing your projects
This second part is about changing the projects displayed on line 8 in `main.py`. It's relatively simple, and all you have to do is to delete the original list and set `db['projects']` to a list of URLs. Be sure to add `?v=1` to the end of your repl attachment.

```py
db['projects'] = ["https://replit.com/@hecker40/firecss?v=1", "https://replit.com/@hecker40/Cookie-Clicker?v=1"]
```

After that, re-run the page and open your website in a new tab. The projects should be updated, and you should be able to see the stats of your repl. This includes likes, runs and comments.

## Editing your blog

I've also implemented a blog feature in which you can release blogs. You can see the function `add_blog(title, desc)` in `main.py` on line 26, and the function being called on line 33 to actually add a blog post. The first parameter is the title, and the second parameter is the description/content of the blog. However, after you use the `add_blog(title, desc)` in your code and run the program, be sure to remove the line of code after running it to avoid the same blog being added twice. This is an important part, so if you are having that problem this part should answer your question.

Well, that's about it folks! I hope this has explained enough, and look forward to seeing you guy's portfolio websites!