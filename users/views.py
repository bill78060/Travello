# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages

# # Create your views here.

# def register_user(request):
#     if request.method =='POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#         if password == password2:
#             if not User.objects.filter(username = username).exists():
#                 if not User.objects.filter(email = email).exists():
#                     user = User.objects.create_user(username=username, email=email, first_name= first_name , last_name= last_name, password= password)
#                     user.save()
#                     return redirect("/")
#                 else:
#                     messages.info(request,'Email already exists')
#             else:
#                 messages.info(request, 'Username aready exists')
#         else:
#             messages.info(request, 'Password and Confirmation Password mismatch')

#     return render(request,'register.html')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Debugging logs
        print("Received POST data:", request.POST)

        if not username or not email or not first_name or not last_name or not password or not password2:
            messages.error(request, 'All fields are required')
            return render(request, 'register.html')  # Re-render the form with an error message
        
        if password == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                    user.save()
                    return redirect("/")
                else:
                    messages.error(request, 'Email already exists')
            else:
                messages.error(request, 'Username already exists')
        else:
            messages.error(request, 'Password and confirmation password mismatch')

    return render(request, 'register.html')




from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(f"Attempting to log in with username: {username}")  # Debug print statement

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful!")  # Success message
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")  # Error message

    return render(request, 'login.html')


def logout_user(request):

    auth.logout(request)

    return redirect('/')





# def login_user(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(usernme=username,password=password)
#         if user:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request, "Invalid Credentials")
#     return render(request, 'login.html')





# def user_logout(request):
#     auth.logout(request)
#     return redirect('/')
