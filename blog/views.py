from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def memo(request):
    return render(request, 'blog/memo.html', {})

def temp(request):
    return render(request, 'blog/temp.html', {})