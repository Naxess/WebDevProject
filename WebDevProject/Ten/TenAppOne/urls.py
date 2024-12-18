from django.urls import path
from TenAppOne import views

app_name = 'tenappone'

urlpatterns = [
    path('', views.language_guides_home_view, name='language_guides_home'),

    path('html_basics/', views.html_basics_view, name='html_basics'),
    path('html_elements_reference/', views.html_elements_reference_view, name='html_elements_reference'),

    path('css_basics/', views.css_basics_view, name='css_basics'),
    path('css_layouts/', views.css_layouts_view, name='css_layouts'),
    path('css_selectors/', views.css_selectors_view, name='css_selectors'),

    path('bootstrap_forms/', views.bootstrap_forms_view, name='bootstrap_forms'),
    path('bootstrap_components/', views.bootstrap_components_view, name='bootstrap_components'),
    path('bootstrap_styling/', views.bootstrap_styling_view, name='bootstrap_styling'),

    path('javascript_basics/', views.javascript_basics_view, name='javascript_basics'),
    path('dom_basics/', views.dom_basics_view, name='dom_basics'),
    path('jquery_basics/', views.jquery_basics_view, name='jquery_basics'),
    path('dom_reference/', views.dom_reference_view, name='dom_reference'),
    path('dom_events_reference/', views.dom_events_reference_view, name='dom_events_reference'),

    path('django_setup/', views.django_setup_view, name='django_setup'),
    path('django_views_and_urls/', views.django_views_and_urls_view, name='django_views_and_urls'),
    path('django_templates/', views.django_templates_view, name='django_templates'),
    path('django_static_files/', views.django_static_files_view, name='django_static_files'),
    path('django_models/', views.django_models_view, name='django_models'),
    path('django_admin_interface/', views.django_admin_interface_view, name='django_admin_interface'),
    path('django_creating_sample_data/', views.django_creating_sample_data_view, name='django_creating_sample_data'),
    path('django_model_queries/', views.django_model_queries_view, name='django_model_queries'),
    path('django_mtv_paradigm/', views.django_mtv_paradigm_view, name='django_mtv_paradigm'),
    path('django_forms/', views.django_forms_view, name='django_forms'),
    path('django_form_validation/', views.django_form_validation_view, name='django_form_validation'),
    path('django_model_forms/', views.django_model_forms_view, name='django_model_forms'),
    path('django_relative_urls/', views.django_relative_urls_view, name='django_relative_urls'),
    path('django_users/', views.django_users_view, name='django_users'),
    path('django_user_login_logout/', views.django_user_login_logout_view, name='django_user_login_logout'),
    path('django_encryption_and_validation/', views.django_ecryption_and_validation_view,
         name='django_encryption_and_validation'),
    path('django_deployment/', views.django_deployment_view, name='django_deployment'),
    path('django_cbvs/', views.django_cbvs_view, name='django_cbvs'),

    path('git_basics/', views.git_basics_view, name='git_basics'),
    path('git_advanced/', views.git_advanced_view, name='git_advanced'),

    path('python/', views.python_view, name='python'),

    path('sql_basics/', views.sql_basics_view, name='sql_basics'),

    path('vim_basics/', views.vim_basics_view, name='vim_basics'),

    path('regex_reference/', views.regex_reference_view, name='regex_reference'),

    path('interview_prep/', views.interview_prep_view, name='interview_prep'),

    path('nodejs_intro_install/', views.nodejs_intro_and_install, name='nodejs_intro_and_install'),
    # path('nodejs_global_variables/', views.nodejs_global_variables, name='nodejs_global_variabls'),
    path('nodejs_express/', views.nodejs_express, name='nodejs_express'),

    path('react_basics/', views.react_basics, name='react_basics'),
    path('react_and_django/', views.react_and_django, name='react_and_django'),
    path('react_examples/', views.react_examples, name='react_examples'),

    path('typescript_intro/', views.typescript_intro, name='typescript_intro'),

    path('typescript_reference/', views.typescript_reference, name='typescript_reference'),
]
