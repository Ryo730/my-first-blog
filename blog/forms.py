from django import forms
from .models import Post
##Formの名前．このフォームがModelFormの一種だとDjangoに伝える役割．
class PostForm(forms.ModelForm):
    #Djangoにフォームを作るときのどのモデルを使えばいいかを伝える（model=Post）
    class Meta:
        model=Post
        #Formのフィールドに何を書くか
        fields=('title','text',)