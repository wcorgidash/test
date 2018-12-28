from django.shortcuts import render

# Create your views here.
def post_list(request):
	return HttpResponse("Hello, you are at the post list index")

def post_detail(request):
	return HttpResponse("Hello, you are at the post detail index")
		