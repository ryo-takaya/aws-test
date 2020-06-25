from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from .models import Post
 
 
class IndexView(generic.ListView): #  generic.ListViewを継承
    model = Post # 使用するモデル
    paginate_by = 5 # 1ページあたりの表示件数をカスタマイズ（学習のため）
    ordering = ['-updated_at'] # 並び順を更新時刻が新しい順にカスタマイズ（学習のため）
    template_name = 'blogs/index.html' # 表示に使用するテンプレート（この後すぐ作成）
 
 
class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/detail.html'
 
 
class CreateView(generic.edit.CreateView):
    model = Post
    fields = '__all__'  
    template_name = 'blogs/create.html'
 
 
class UpdateView(generic.edit.UpdateView):
    model = Post
    fields = '__all__' 
    template_name = 'blogs/update.html'
 
 
class DeleteView(generic.edit.DeleteView):
    model = Post
    success_url = reverse_lazy('blogs:index') 
    template_name = 'blogs/delete.html'