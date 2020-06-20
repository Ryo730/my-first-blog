##モデルのフィールドや定義の仕方は以下ドキュメント参照
#https://docs.djangoproject.com/ja/2.2/ref/models/fields/#field-types
from django.db import models
from django.conf import settings
from django.utils import timezone

##This is Object
#ポストがDjango modelyとしている．Djangoが，これはデータベースに保存すべきものだとわかるようにするため
class Post(models.Model):
    ##プロパティ（状態）の設定
    #他のモデルへのリンク
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #文字数が制限されたテキストを定義するフィールド
    title=models.CharField(max_length=200)
    #制限なしの長いテキスト用のフィールド
    text=models.TextField()
    #models.DataTimeField→日付と時間のフィールド
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    ##メソッド（命令）の設定
    #ブログを公開するメソッド
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    #これを呼ぶとポストのタイトルのテキストが返ってくる
    def __str__(self):
        return self.title