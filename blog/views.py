from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post,My_post
from .forms import PostForm,My_postform
from django.contrib import messages

# Create your views here.
def post_list(request):
	#フィルタで条件にあうオブジェクトを検索
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	print("posts:",posts)
	return render(request, 'blog/post_list.html', {'posts': posts})

def memo(request):
	#指定のhtmlファイルを呼び出し
	#print("memo")
	return render(request, 'blog/memo.html')

def temp(request):
	return render(request, 'blog/temp.html')

def post_detail(request, pk):
	print(pk)
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	#form = PostForm()
	#return render(request, 'blog/post_edit.html', {'form': form})
	if request.method == "POST":
		#新しくpostをsave下処理
		#print("POSTchan")
		form = PostForm(request.POST)
		#内容があるか
		if form.is_valid():
			print("save")
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		print("change")
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		#維持
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def mypage(request):
	form = My_postform(request.POST or None)
	if request.method == 'POST':
		print("write!!")
		if form.is_valid():
			form.save()
			messages.success(request,'お疲れ様でした')
			return redirect('test')
		else :
			messages.error(request,'エラー')
	post = My_post.objects.order_by('published_date')

	contexts = {
		'form': form,
		'post': post,
	}

	return render(request, 'blog/my_page_front.html',contexts)

'''	
def delete(request,otitle):
    if request.method == 'POST':
        # ボタンがクリックされた場合の処理
        #My_post.objects.filter(title=otitle).delete()
        print(My_post.objects)
    return render(request, 'blog/test.html')
    <!-- <a class="btn btn-default" href="{% url 'delete' otitle=posting.title %}"><span class="glyphicon glyphicon-pencil"></span></a> -->
'''

#テスト用
def test(request):
	print(request)
	form = My_postform(request.POST or None)
	print("ok1")
	if request.method == 'POST':
		print("write!!")
		if form.is_valid():
			form.save()
			print(form.fields)
			messages.success(request,'お疲れ様でした')
			return redirect('test')
		else :
			messages.error(request,'エラー')
	post = My_post.objects.order_by('published_date')

	contexts = {
		'form': form,
		'post': post,
	}
	print(contexts)

	return render(request, 'blog/test.html',contexts)
