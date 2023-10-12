from django.shortcuts import redirect
from django.urls import reverse
# from django.middleware.common import CommonMiddleware


# class ExceptionMiddleware(CommonMiddleware):
#     def process_exception(self, request, exception):
#         return redirect('login')  


# class MyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Code xử lý trước khi request được gửi tới view

#         response = self.get_response(request)

#         # Code xử lý sau khi response được trả về client

#         return response
