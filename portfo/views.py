
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404 ,redirect, render
from portfo.models  import Posts,Category
from .forms import CommentForm
from django.shortcuts import render
from django.core.mail import send_mail
from .form1 import ContactForm
from .models import ArtifactReflection
from django.core.paginator import Paginator

def index(request):
     artifacts = ArtifactReflection.objects.all()
     paginator = Paginator(artifacts, 4)
     page_number = request.GET.get('page')
     artifacts = paginator.get_page(page_number)
     return render(request,'index.html',{'artifacts': artifacts})

def comp(request):
   posts = Posts.objects.filter(status=Posts.ACTIVE)
   return render(request, 'frontpage.html',{'posts':posts})

def detail(request, category_slug, slug):
    post = get_object_or_404(Posts,slug=slug,status=Posts.ACTIVE)
    
    form = CommentForm(request.POST)

    if form.is_valid():
      comment =  form.save(commit=False)
      comment.post = post
      comment.save()
      return redirect('post_detail',slug=slug)
    else:
        form = CommentForm()
        return render(request, 'detail.html',{'post':post,'form':form})
    
def category(request,slug):
     category = get_object_or_404(Category,slug=slug)
     posts = category.posts.filter(status=Posts.ACTIVE)
     return render(request,'category.html',{'category':category,'posts':posts})

def search(request):
    query = request.GET.get('query','')

    posts = Posts.objects.filter(status=Posts.ACTIVE).filter(Q(title__icontains=query)| Q(intro__icontains=query)|Q(body__icontains=query))

    return render(request,'search.html',{'posts':posts,'query':query})

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            fon_number = form.CharField(max_length=15)
            message = form.cleaned_data['message']

            # Send the email
            send_mail(
                f"New message from {name}",
                message,
                email,
                ['musinachirevotafadzwa@gmail.com'],  # Replace with your email
                fail_silently=False,
            )
            form = ContactForm()  # Reset the form after successful submission
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})

# Here
def artifact_detail(request, id):
    artifact = get_object_or_404(ArtifactReflection,id=id)
    return render(request, 'artifact_detail.html', {'artifact': artifact})