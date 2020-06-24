from django.urls import path
from . import views

##Djangoのpathk関数とblogアプリのすべてのビューをインポートする
#見てのとおり、post_list という名前の ビュー をルートURLに割り当てています。 このURLパターンは空の文字列に一致します。
#Djangoはビューを見つけるとき、URLのパス(path)の前にくっつくドメイン名（つまり、http://127.0.0.1:8000/ の部分）を無視します。
#このパターンは誰かがあなたのWebサイトの 'http://127.0.0.1:8000/' というアドレスにアクセスしてきたら views.post_list が正しい行き先だということをDjangoに伝えます。
urlpatterns=[
    path('',views.post_list,name='post_list'),
    #post/はURLがpostに続けて/で始まることを意味する．
    #<int:pk>これはDjangoは整数の値を期待し、その値がpkという名前の変数でビューに渡されることを意味しています。
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
]
##practice for github