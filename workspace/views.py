import urllib3
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
import json

from .forms import PotentialForm, HardSpherePotentialForm, DynamicModuleForm

# Modificar la IP y el Número de Puerto de Acuerdo al Servidor
DIR_IP = '192.168.4.60:'
PUERTO = '5002'


def request_string(a_method, a_string):
    http = urllib3.PoolManager()
    res = http.request(a_method, a_string)
    return res

# Filtra la lista con solamente los arhivos dfe texto
def filter_list(a_list_with_out_filter):
    list_aux = []

    for item in a_list_with_out_filter:
        if not (str(item).find('.png') > 0):
            list_aux.append(item)
    return list_aux

@login_required
def workspace(request):
    return render(request, 'workspace.html')

@login_required
def hard_sphere(request):
    if request.method == "POST":
        form = HardSpherePotentialForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.potential = 1
            post.temp = 0
            post.id_user_id = request.user.id
            post.created_at = timezone.now()
            # print('Valor de Phi = ')
            # print(post.phi)
            url = DIR_IP + PUERTO + '/exe_hard_sphere/' + request.user.username + '/' + str(post.phi)
            try:
                res = request_string('GET', url)
                if res.status == 200:
                    post.save()
                    messages.success(request, 'Tus Datos de han Enviado Correctamente')
                    return redirect('hard_sphere')
            except urllib3.exceptions.MaxRetryError:
                print('The maximum number of retries is exceeded.')
                num_error = 500
                message = 'The maximum number of retries is exceeded.'
                return render(request, 'errors.html', {'num_error':  num_error, 'message': message})
            except urllib3.exceptions.ConnectTimeoutError:
                print('A socket timeout occurs while connecting to a server.')
                num_error = 401
                message = 'A socket timeout occurs while connecting to a server.'
                return render(request, 'errors.html', {'num_error':  num_error, 'message': message})
    else:
        form = HardSpherePotentialForm()
    return render(request, 'form_hard_sphere.html', {'form': form})

@login_required
def soft_sphere(request):
    if request.method == "POST":
        form = PotentialForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.potential = 2
            post.id_user_id = request.user.id
            post.created_at = timezone.now()
            url = DIR_IP + PUERTO + '/exe_soft_sphere/' + request.user.username + '/' + str(post.phi) + '/' + str(post.temp)
            try:
                res = request_string('GET', url)
                if res.status == 200:
                    post.save()
                    messages.success(request, 'Tus Datos de han Enviado Correctamente')
                    return redirect('soft_sphere')
            except urllib3.exceptions.MaxRetryError:
                print('The maximum number of retries is exceeded.')
                num_error = 500
                message = 'The maximum number of retries is exceeded.'
                return render(request, 'errors.html', {'num_error':  num_error, 'message': message})
            except urllib3.exceptions.ConnectTimeoutError:
                print('A socket timeout occurs while connecting to a server.')
                num_error = 401
                message = 'A socket timeout occurs while connecting to a server.'
                return render(request, 'errors.html', {'num_error':  num_error, 'message': message})
    else:
        form = PotentialForm()
    return render(request, 'form_soft_sphere.html', {'form': form})

@login_required
def yukawa(request):
    if request.method == "POST":
        form = PotentialForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.potential = 3
            post.id_user_id = request.user.id
            post.created_at = timezone.now()
            url = DIR_IP + PUERTO + '/exe_Yukawa/' + request.user.username + '/' + str(post.phi) + '/' + str(post.temp)
            try:
                res = request_string('GET', url)
                if res.status == 200:
                    post.save()
                    messages.success(request, 'Tus Datos de han Enviado Correctamente')
                    return redirect('yukawa')
            except urllib3.exceptions.MaxRetryError:
                print('The maximum number of retries is exceeded.')
                num_error = 500
                message = 'The maximum number of retries is exceeded.'
                return render(request, 'errors.html', {'num_error':  num_error, 'message': message})
            except urllib3.exceptions.ConnectTimeoutError:
                print('A socket timeout occurs while connecting to a server.')
                num_error = 401
                message = 'A socket timeout occurs while connecting to a server.'
                return render(request, 'errors.html', {'num_error':  num_error, 'message': message})
    else:
        form = PotentialForm()
    return render(request, 'form_yukawa.html', {'form': form})

@login_required
def dynamic_module(request):
    if request.method == "POST":
        form = DynamicModuleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_user_id = request.user.id
            post.created_at = timezone.now()
            url = DIR_IP + PUERTO + '/exe_dynamic_module/' + request.user.username + '/' + str(post.phi)
            try:
                res = request_string('GET', url)
                if res.status == 200:
                    post.save()
                    messages.success(request, 'Tus Datos de han Enviado Correctamente')
                    return redirect('dynamic_module')
            except urllib3.exceptions.MaxRetryError:
                print('The maximum number of retries is exceeded.')
                num_error = 500
                message = 'The maximum number of retries is exceeded.'
                return render(request, 'errors.html', {'num_error':  num_error, 'message': message})
            except urllib3.exceptions.ConnectTimeoutError:
                print('A socket timeout occurs while connecting to a server.')
                num_error = 401
                message = 'A socket timeout occurs while connecting to a server.'
                return render(request, 'errors.html', {'num_error':  num_error, 'message': message})
    else:
        form = DynamicModuleForm()
    return render(request, 'dynamic_module.html', {'form': form})


@login_required
def hard_sphere_data(request):
    url = DIR_IP + PUERTO + '/get_files/' + request.user.username + '/' + 'Esfera_Dura'
    print(url)
    try:
        res = request_string('GET', url)
        if res.status == 200:
            aux = json.loads(res.data.decode('utf-8'))
            list = aux['Esfera_Dura']
            list = filter_list(list)
            # print(list)
            messages.success(request, 'Datos Recuperados Correctamente')
    except urllib3.exceptions.MaxRetryError:
        print('The maximum number of retries is exceeded.')
        num_error = 500
        message = 'The maximum number of retries is exceeded.'
        return render(request, 'errors.html', {'num_error': num_error, 'message': message})
    except urllib3.exceptions.ConnectTimeoutError:
        print('A socket timeout occurs while connecting to a server.')
        num_error = 401
        message = 'A socket timeout occurs while connecting to a server.'
        return render(request, 'errors.html', {'num_error': num_error, 'message': message})
    return render(request, 'hard_sphere_data.html', {'list': list})


@login_required
def soft_sphere_data(request):
    url = DIR_IP + PUERTO + '/get_files/' + request.user.username + '/' + 'Esfera_Suave'
    try:
        res = request_string('GET', url)
        if res.status == 200:
            aux = json.loads(res.data.decode('utf-8'))
            list = aux['Esfera_Suave']
            list = filter_list(list)
            # print(list)
            messages.success(request, 'Datos Recuperados Correctamente')
    except urllib3.exceptions.MaxRetryError:
        print('The maximum number of retries is exceeded.')
        num_error = 500
        message = 'The maximum number of retries is exceeded.'
        return render(request, 'errors.html', {'num_error': num_error, 'message': message})
    except urllib3.exceptions.ConnectTimeoutError:
        print('A socket timeout occurs while connecting to a server.')
        num_error = 401
        message = 'A socket timeout occurs while connecting to a server.'
        return render(request, 'errors.html', {'num_error': num_error, 'message': message})
    return render(request, 'soft_sphere_data.html', {'list': list})

@login_required
def yukawa_data(request):
    url = DIR_IP + PUERTO + '/get_files/' + request.user.username + '/' + 'Yukawa'
    try:
        res = request_string('GET', url)
        if res.status == 200:
            aux = json.loads(res.data.decode('utf-8'))
            list = aux['Yukawa']
            list = filter_list(list)
            # print(list)
            messages.success(request, 'Datos Recuperados Correctamente')
    except urllib3.exceptions.MaxRetryError:
        print('The maximum number of retries is exceeded.')
        num_error = 500
        message = 'The maximum number of retries is exceeded.'
        return render(request, 'errors.html', {'num_error': num_error, 'message': message})
    except urllib3.exceptions.ConnectTimeoutError:
        print('A socket timeout occurs while connecting to a server.')
        num_error = 401
        message = 'A socket timeout occurs while connecting to a server.'
        return render(request, 'errors.html', {'num_error': num_error, 'message': message})
    return render(request, 'yukawa_data.html', {'list': list})

@login_required
def dynamic_data(request):
    url = DIR_IP + PUERTO + '/get_files/' + request.user.username + '/' + 'Dinamico'
    try:
        res = request_string('GET', url)
        if res.status == 200:
            aux = json.loads(res.data.decode('utf-8'))
            list = aux['Dinamico']
            list = filter_list(list)
            # print(list)
            messages.success(request, 'Datos Recuperados Correctamente')
    except urllib3.exceptions.MaxRetryError:
        print('The maximum number of retries is exceeded.')
        num_error = 500
        message = 'The maximum number of retries is exceeded.'
        return render(request, 'errors.html', {'num_error': num_error, 'message': message})
    except urllib3.exceptions.ConnectTimeoutError:
        print('A socket timeout occurs while connecting to a server.')
        num_error = 401
        message = 'A socket timeout occurs while connecting to a server.'
        return render(request, 'errors.html', {'num_error': num_error, 'message': message})
    return render(request, 'dynamic_module_data.html', {'list': list})

@login_required
def dynamic_data_content(request, directory):
    url = DIR_IP + PUERTO + '/get_files_dynamic/' + request.user.username + '/' + directory
    try:
        res = request_string('GET', url)
        if res.status == 200:
            aux = json.loads(res.data.decode('utf-8'))
            list = aux[directory]
            list = filter_list(list)
            # print(list)
            # print('Directorio')
            # print(directory)
            messages.success(request, 'Datos Recuperados Correctamente')
    except urllib3.exceptions.MaxRetryError:
        print('The maximum number of retries is exceeded.')
        num_error = 500
        message = 'The maximum number of retries is exceeded.'
        return render(request, 'errors.html', {'num_error': num_error, 'message': message})
    except urllib3.exceptions.ConnectTimeoutError:
        print('A socket timeout occurs while connecting to a server.')
        num_error = 401
        message = 'A socket timeout occurs while connecting to a server.'
        return render(request, 'errors.html', {'num_error': num_error, 'message': message})
    return render(request, 'dynamic_module_data_content.html', {'list': list, 'directory': directory})
