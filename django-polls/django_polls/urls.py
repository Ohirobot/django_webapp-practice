from django.urls import path

from . import views

# 'app_name'としてアプリケーションごとの名前空間を定義することで、別アプリ内に同名のURLがあっても区別できる。
app_name = "polls"
urlpatterns = [
    # 'name'の値はテンプレート内の{% url %}タグで呼び出される。
    # ex: /polls/
    #汎用ビューを使用しない場合：path("", views.index, name="index"),
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    #汎用ビューを使用しない場合：path("<int:question_id>/", views.detail, name="detail"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    #汎用ビューを使用しない場合：path("<int:question_id>/results/", views.results, name="results"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]