# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 
from django.shortcuts import render_to_response

def post_list(request):
    post_list = Post.objects.all()
    
    my_context = Context({'posts':post_list})   # this means put the postlist info into a dictionary called posts
    return render_to_response ('blog/post_list.html', my_context)
   
class CommentForm(ModelForm):
   class Meta:
     exclude=['post']
     model=Comment

@csrf_exempt
def post_detail(request, id, showComments=False):
    p=Post.objects.get(pk=id)
    if request.method == 'POST':
       comment = Comment(post=p)
       form = CommentForm(request.POST, instance=comment)
       if form.is_valid():
          form.save()
       return HttpResponseRedirect(request.path)
    else:
       form = CommentForm()  # empty comment form
    
    	    
    for i in p.commentsss.all():  # the commentsss  here is in the model as a related name in the class Comment
      
      my_context = Context({'post':p,'comments':p.commentsss.all(),'form':form})
    
    return render_to_response ('blog/post_detail.html', my_context)  
 



@csrf_exempt
def edit_comment(request,id):
   q=Comment.objects.get(pk=id)
   if request.method == 'POST':
    
       form = CommentForm(request.POST, instance=q)  # the instance here equates whatever is in q to the CommentForm.
       if form.is_valid():
           form.save()
       return HttpResponseRedirect(request.path)     # redirects the user to the page with his comments data
   else:
       form = CommentForm(instance=q)          # the instance equates the q to the CommentForm ie. gives the already populated CommentForm 


   my_context = Context({'commentedit':q,'form':form})
    
   return render_to_response ('blog/edit_comment.html',my_context)  

  



def post_search(request, term=True):
     p=Post.objects.filter(body__contains=term)
         
     my_context = Context({'posts':p,'term':term})
     return render_to_response ('blog/post_search.html', my_context)
    


def home(request):
     return render_to_response('blog/base.html',{})
 
