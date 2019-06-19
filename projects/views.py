from django.shortcuts import render

from .forms import SignInForm, CreateAccountForm, CreateProjectForm, CreateTaskForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import Http404

from projects.models import Project, Task
from django.contrib.auth.models import User

def index(request):
	user = request.user

	if user.is_authenticated:
		project_list = Project.objects.filter(user=user)
		context = {
			'project_list': project_list
		}
		return render(request, 'projects/index.html', context)
	else:
		return redirect('/projects/sign-in/')

'''
def sign_in(request):
	if request.method == 'POST':
		form = SignInForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)

				return redirect('/projects/home/')

			else:
				form = SignInForm()
				return render(request, 'projects/sign-in.html', {'form': form})
	else:
		form = SignInForm()
    
	return render(request, 'projects/sign-in.html', {'form': form})
'''

def sign_out(request):
	logout(request)

	return redirect('/projects/home/')

def create_account(request):
	if request.method == 'POST':
		form = CreateAccountForm(request.POST)

		if form.is_valid():
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = User.objects.create_user(username=username, email=None, password=password)

			user.first_name = firstname
			user.last_name = lastname

			user.save()

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)

				return redirect('/projects/')

			else:
				form = SignInForm()
				return render(request, 'projects/sign-in.html', {'form': form})

	else:
		form = CreateAccountForm()

	return render(request, 'projects/create-account.html', {'form': form})

def delete_account(request):
	user = request.user

	user.delete()

	return redirect('/projects/sign-in/')

def create_project(request):
	if request.method == 'POST':
		form = CreateProjectForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name']
			user = request.user

			new_project = Project(name=name, user=user)

			new_project.save()

			return redirect('/projects/')
	else:
		form = CreateProjectForm()

	return render(request, 'projects/create-project.html', {'form': form})	
	
def delete_project(request, project_id):
	try:
		project = Project.objects.get(pk=project_id)
	except Project.DoesNotExist:
		raise Http404("Project does not exist")
	
	project.delete()
	
	return redirect('/projects/')

def project_detail(request, project_id):
	user = request.user
	if user.is_authenticated:
		try:
			project = Project.objects.get(pk=project_id)
		except Project.DoesNotExist:
			raise Http404("Project does not exist")

		task_list = Task.objects.filter(project=project)

		context = {
			'project': project,
			'task_list': task_list
		}

		return render(request, 'projects/project-detail.html', context)
	else:
		return redirect('/projects/sign-in/')

def home(request):
	user = request.user
	userStatus = user.is_authenticated
	userName = user.get_username()

	if userStatus:
		userName = user.get_short_name()



	if request.method == 'POST':
		form = SignInForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				userStatus = user.is_authenticated
				userName = user.get_short_name()

			else:
				form = SignInForm()
				return render(request, 'projects/sign-in.html', {'form': form})
	else:
		form = SignInForm()

	return render(request, 'projects/home.html', {'userStatus': userStatus, 'userName': userName, 'form': form})

def create_task(request, project_id):
	if request.method == 'POST':
		form = CreateTaskForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name']
			project = Project.objects.get(pk=project_id)

			new_task = Task(name=name, project=project)

			new_task.save()

			return redirect('/projects/' + str(project_id))

	else:
		form = CreateTaskForm()

	return render(request, 'projects/create-task.html', {'form': form})

def delete_task(request, project_id, task_id):
	user = request.user
	if user.is_authenticated:
		try:
			task = Task.objects.get(pk=task_id)
		except Task.DoesNotExist:
			raise Http404("Task does not exist")
		
		task.delete()
		
		return redirect('/projects/' + str(project_id))
	else:
		return redirect('/projects/sign-in')


def task_detail(request, project_id, task_id):
	user = request.user
	if user.is_authenticated:
		try:
			project = Project.objects.get(pk=project_id)
		except Project.DoesNotExist:
			raise Http404("Project does not exist")

		task = Task.objects.get(pk=task_id)

		context = {
			'project' : project,
			'task': task
		}

		return render(request, 'projects/task-detail.html', context)
	else:
		return redirect('/projects/sign-in/')





	


