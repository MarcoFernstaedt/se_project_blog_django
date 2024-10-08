from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

posts = [
  {
    "id": 1,
    "title": "The Future of Web Development",
    "content": "Web development is constantly evolving, with new frameworks, tools, and techniques emerging every day. In this post, we explore what the future holds for the industry and how developers can stay ahead of the curve."
  },
  {
    "id": 2,
    "title": "Understanding React Hooks",
    "content": "React Hooks have revolutionized the way we write functional components in React. This guide will take you through the basics of hooks, explaining how to use useState, useEffect, and other popular hooks in your projects."
  },
  {
    "id": 3,
    "title": "Top 10 JavaScript Libraries in 2024",
    "content": "JavaScript has a massive ecosystem of libraries that make development easier and more efficient. Here, we list the top 10 libraries every developer should know in 2024, including their use cases and benefits."
  },
  {
    "id": 4,
    "title": "Why You Should Learn Python in 2024",
    "content": "Python has consistently ranked as one of the most popular programming languages due to its versatility and ease of use. In this post, we discuss why learning Python is a smart career move for 2024 and beyond."
  },
  {
    "id": 5,
    "title": "Building Scalable APIs with Node.js",
    "content": "In the world of microservices and distributed systems, building scalable APIs is critical. This post covers best practices for designing and building APIs using Node.js, ensuring they can handle high traffic and loads."
  }
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def getPostById(request, id):
    id_isValid = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            id_isValid = True
            break
    
    if id_isValid:
        return HttpResponse(post_dict)
    else:
        return HttpResponseNotFound("Post Not Available")
    
def findPost(request, id):
    url = reverse('post', args=[id])
    return HttpResponseRedirect(url)