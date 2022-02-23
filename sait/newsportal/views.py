from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, View, DeleteView
from django.core.paginator import Paginator
from .models import Post, Category
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm


class Newsportal(View):
    def get(self, request):
        news = Newsportal.objects.order_by('-price')
        p = Paginator(news, 1)  # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы
        newsportal = p.get_page(request.GET.get('page', 1))  # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами
        data = {
            'newsportal': newsportal,
                }
        return render(request, 'newsportal.html', data)

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'newsportal.html'  # указываем имя шаблона, где будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'newsportal'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    #queryset = Post.objects.order_by('-id')  # настроили пораметр отображения более новый продукт
    ordering = ['-price']
    paginate_by = 1


    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        #context['categories'] = Category.objects.all()
        return context


    # дженерик для получения деталей о товаре
class PostDetailView(DetailView):
    template_name = 'newsportal/Post_detail.html'
    queryset = Post.objects.all()


    # дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(CreateView):
    template_name = 'newsportal/Post_create.html'
    form_class = PostForm

    # дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    template_name = 'newsportal/Post_create.html'
    form_class = PostForm

        # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    # дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'newsportal/Post_delete.html'
    queryset = Post.objects.all()
    success_url = '/newsportal/'






""" test"""
"""from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'newsportal.html'  # указываем имя шаблона, где будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'newsportal'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')  # настроили пораметр отображения более новый продукт

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
"""