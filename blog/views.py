from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .forms import *
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
		#他のページから飛んできた時
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

########################################

def mypage(request):
	print(request.method)
	if request.method == 'POST':
		if 'save' in request.POST:
			form = My_postform(request.POST)
			print("write!!")
			if form.is_valid():
				form.save()
				print(form.fields)
				messages.success(request,'お疲れ様でした')
				return redirect('mypage')
		elif 'trend' in request.POST:
			trend = My_trendform(request.POST)
			print("write_tr!!")
			if trend.is_valid():
				trend.save()
				#print(form.fields)
				messages.success(request,'お疲れ様でした')
				return redirect('mypage')
		elif 'task' in request.POST:
			task = My_taskform(request.POST)
			print("write_ta!!")
			if task.is_valid():
				task.save()
				#print(form.fields)
				messages.success(request,'お疲れ様でした')
				return redirect('mypage')
		elif 'interest' in request.POST:
			interest = My_interestform(request.POST)
			print("write_in!!")
			if interest.is_valid():
				interest.save()
				#print(form.fields)
				messages.success(request,'お疲れ様でした')
				return redirect('mypage')
		else :
			#form = My_postform()
			messages.error(request,'エラー')
	else :
		#print("remain")
		form = My_postform()
		trend = My_trendform()
		task = My_taskform()
		interest = My_interestform()

	post = My_post.objects.order_by('published_date')
	post_trend = My_trend.objects.order_by('published_date')
	post_task = My_task.objects.order_by('published_date')
	post_interest = My_interest.objects.order_by('published_date')

	contexts = {
		'form': form,
		'trend': trend,
		'task': task,
		'interest' : interest,
		'post': post,
		'post_trend':post_trend,
		'post_task':post_task,
		'post_interest':post_interest,
	}
	#print(contexts)

	return render(request, 'blog/my_page_front.html',contexts)


def delete(request,otitle):
	print("del action")
	#print(request.POST)
	if request.method == 'POST':
		# ボタンがクリックされた場合の処理
		if 'button_del' in request.POST:
			print("delete!")
			messages.success(request,'デリート!')
			My_post.objects.filter(title=otitle).delete()
			return redirect('mypage')
		elif 'del_task' in request.POST:
			print("delete!")
			messages.success(request,'デリート!')
			My_task.objects.filter(topic=otitle).delete()
			return redirect('mypage')
		elif 'del_trend' in request.POST:
			print("delete!")
			messages.success(request,'デリート!')
			My_trend.objects.filter(topic=otitle).delete()
			return redirect('mypage')
		elif 'del_interest' in request.POST:
			print("delete!")
			messages.success(request,'デリート!')
			My_interest.objects.filter(topic=otitle).delete()
			return redirect('mypage')

	return render(request, 'blog/my_page_front.html')

def input_trend(request,input):
	print("trend")
	return render(request, 'blog/my_page_front.html')

#テスト用
def test(request):
	print("リクエスト:",request.POST)
	#trend = My_trendform(re)
	#書き込みなどできた場合
	print(request.method)
	if request.method == 'POST':
		if 'save' in request.POST:
			form = My_postform(request.POST)
			print("write!!")
			if form.is_valid():
				form.save()
				print(form.fields)
				messages.success(request,'お疲れ様でした')
				return redirect('test')
		elif 'trend' in request.POST:
			trend = My_trendform(request.POST)
			print("write_tr!!")
			if trend.is_valid():
				trend.save()
				#print(form.fields)
				messages.success(request,'お疲れ様でした')
				return redirect('test')
		elif 'task' in request.POST:
			task = My_taskform(request.POST)
			print("write_ta!!")
			if task.is_valid():
				task.save()
				#print(form.fields)
				messages.success(request,'お疲れ様でした')
				return redirect('test')
		elif 'interest' in request.POST:
			interest = My_interestform(request.POST)
			print("write_in!!")
			if interest.is_valid():
				interest.save()
				#print(form.fields)
				messages.success(request,'お疲れ様でした')
				return redirect('test')
		else :
			#form = My_postform()
			messages.error(request,'エラー')
	else :
		#print("remain")
		form = My_postform()
		trend = My_trendform()
		task = My_taskform()
		interest = My_interestform()

	post = My_post.objects.order_by('published_date')
	post_trend = My_trend.objects.order_by('published_date')
	post_task = My_task.objects.order_by('published_date')
	post_interest = My_interest.objects.order_by('published_date')

	contexts = {
		'form': form,
		'trend': trend,
		'task': task,
		'interest' : interest,
		'post': post,
		'post_trend':post_trend,
		'post_task':post_task,
		'post_interest':post_interest,
	}
	#print(contexts)

	return render(request, 'blog/test.html',contexts)
