from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index' ),
    path('package/', views.package,name='package'),
    path('blog/', views.blog,name='blog'),
    path('branch/', views.branches,name='branch'),
    path('gallery/', views.gallery,name='gallery'),
    path('executive-package/', views.executive_package,name='executive-package'),
    path('ayush-general/', views.ayush_general,name='ayush-general'),
    path('ayush-silver-plan/', views.ayush_silver,name='ayush-silver-plan'),
    path('ayush-gold/', views.ayush_gold,name='ayush-gold'),
    path('ayush-diabetic/', views.ayush_diabetic,name='ayush-diabetic'),
    path('cardiac/', views.cardiac,name='cardiac'),
    path('executive-package/', views.executive_package,name='executive-package'),
    path('gmrl-chambakkara/', views.gmrl_chambakkara,name='gmrl-chambakkara'),
    path('gmrl-vadakan/', views.gmrl_vadakkekotta,name='gmrl-vadakan'),
    path('gmrl-kolencherry/', views.gmrl_kolenchery,name='gmrl-kolencherry'),
    path('gmrl-thrippunithura/', views.gmrl_thrippunithura,name='gmrl-thrippunithura'),
    path('molecular/', views.moleculor_biology,name='molecular'),
    path('radiology/', views.radiology,name='radiology'),
    path('test/', views.test,name='test'),
    path('contact/', views.contact,name='contact'),
    path('appointment/', views.appointment,name='appointment'),
    path('about/',views.about,name='about'),
    path('privacy/',views.privacy,name='privacy.html'),
    path('terms/',views.terms_condition,name='terms.html')
    






    
]
