from django.urls import *
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path("index/",views.index,name="index"),
    path("login/",views.userlogin,name="login"),
    path("book/",views.bookdetail,name='book'),
    path("signup/",views.usersingup,name="singup"),
    path("show/",views.userprofile,name='show'),
    path("logout/",views.userlogout,name="logout"),
    path("changepass",views.changepass,name="changepass"),
    path("sorting/",views.booksort,name="sorting"),
    path("adddata/",views.addbooks,name="adddata"),
    path("searching/",views.search,name="searching"),
    path("add/",views.addbookauth,name="add"),
    path("addauth/",views.addauthor,name="addauth"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('<int:id>/',views.update,name="update"),
    path("buy/<int:id>",views.buy,name="buy"),
    path("buy/",views.afterbuy,name="buy"),
    path('deletecart/<int:id>/', views.deletecart, name='deletecart'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)