from django.urls import path
from django.contrib.auth import views as auth_views
from .views import book_list, book_create, book_update, book_delete, register, login_view, logout_view, user_profile, add_to_cart, update_cart, view_cart, \
checkout, remove_from_cart, order_detail

urlpatterns = [
    # Страница регистрации
    path('register/', register, name='register'),

    # Стандартная страница входа
    path('login/', login_view, name='login'),

    # Страница выхода
    path('logout/', logout_view, name='logout'),

    # Главная страница с книгами (доступна после логина)
    path('', book_list, name='book_list'),

    # Страница создания книги (доступна только для авторизованных)
    path('book/create/', book_create, name='book_create'),

    # Страница редактирования книги
    path('book/<int:pk>/update/', book_update, name='book_update'),

    # Страница удаления книги
    path('book/<int:pk>/delete/', book_delete, name='book_delete'),

    # Личный кабинет
    path('profile/', user_profile, name='profile'),

    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),

    path('update_cart/', update_cart, name='update_cart'),  # Обновление корзины

    path('cart/', view_cart, name='view_cart'),

    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    
    path('checkout/', checkout, name='checkout'),
    
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
]
