from django .urls import path
from .import views

urlpatterns=[
    path('',views.base,name='base'),
    path('company',views.company,name='company'),
    path('stock_group',views.stock_group,name='stock_group'),
    path('stock_category_creation',views.stock_category_creation,name='stock_category_creation'),
    path('unit_creation',views.unit_creation,name='unit_creation'),
    path('godown_alteration',views.godown_alteration,name='godown_alteration'),
    path('employee_creation',views.employee_creation,name='employee_creation'),
    path('employee_group_cretation',views.employee_group_cretation,name='employee_group_cretation')
]


