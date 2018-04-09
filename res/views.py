from django.http import Http404
from  .models import Category, Item , Order
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate , login
from django.views import generic
from django.views.generic import View
from .forms import UsrForm


class IndexView(generic.ListView) :
    template_name = 'res/index.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()


def detail(request, category_name):
    try:
        category = Category.objects.get(category_title = category_name)
        all_categories = Category.objects.all()
        items = category.items.all()
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    return render(request, 'res/menu.html', {'items': items,'all_categories': all_categories})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'res/login.html')
    else:
        return render(request, 'res/home.html')


class UserFormView(View):
    form_class = UsrForm
    template_name = 'res/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request , self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username , password=password)

            if user is not None:
                if user.is_active:
                    login(request , user)
                    return redirect('res : index')

        return render(request, self.template_name, {'form': form})


