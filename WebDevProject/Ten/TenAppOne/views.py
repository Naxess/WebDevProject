from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def language_guides_home_view(request):
    return render(request, 'TenAppOne/language_guides_home.html')


def html_basics_view(request):
    return render(request, 'TenAppOne/html_basics.html')


def html_elements_reference_view(request):
    return render(request, 'TenAppOne/html_elements_reference.html')


def css_basics_view(request):
    return render(request, 'TenAppOne/css_basics.html')


def css_layouts_view(request):
    return render(request, 'TenAppOne/css_layouts.html')


def css_selectors_view(request):
    return render(request, 'TenAppOne/css_selectors.html')


def bootstrap_forms_view(request):
    return render(request, 'TenAppOne/bootstrap_forms.html')


def bootstrap_components_view(request):
    return render(request, 'TenAppOne/bootstrap_components.html')


def bootstrap_styling_view(request):
    return render(request, 'TenAppOne/bootstrap_styling.html')


@login_required()
def javascript_basics_view(request):
    return render(request, 'TenAppOne/javascript_basics.html')


@login_required()
def dom_basics_view(request):
    return render(request, 'TenAppOne/dom_basics.html')


@login_required()
def dom_reference_view(request):
    return render(request, 'TenAppOne/dom_reference.html')


@login_required()
def dom_events_reference_view(request):
    return render(request, 'TenAppOne/dom_events_reference.html')


@login_required()
def django_setup_view(request):
    return render(request, 'TenAppOne/django_setup.html')


@login_required()
def django_views_and_urls_view(request):
    return render(request, 'TenAppOne/django_views_and_urls.html')


@login_required()
def django_templates_view(request):
    context = {'ifchanged_dict': [1, 2, 1, 2, 2]}
    return render(request, 'TenAppOne/django_templates.html', context)


@login_required()
def django_static_files_view(request):
    return render(request, 'TenAppOne/django_static_files.html')


@login_required()
def django_models_view(request):
    return render(request, 'TenAppOne/django_models.html')


@login_required()
def django_admin_interface_view(request):
    return render(request, 'TenAppOne/django_admin_interface.html')


@login_required()
def django_creating_sample_data_view(request):
    return render(request, 'TenAppOne/django_creating_sample_data.html')


@login_required()
def django_model_queries_view(request):
    return render(request, 'TenAppOne/django_model_queries.html')


@login_required()
def django_mtv_paradigm_view(request):
    test_list = [1, 2, 3, 4]
    return render(request, 'TenAppOne/django_mtv_paradigm.html', context={'test_one': test_list})


@login_required()
def django_forms_view(request):
    return render(request, 'TenAppOne/django_forms.html')


@login_required()
def django_form_validation_view(request):
    return render(request, 'TenAppOne/django_form_validation.html')


@login_required()
def django_model_forms_view(request):
    return render(request, 'TenAppOne/django_model_forms.html')


@login_required()
def django_relative_urls_view(request):
    return render(request, 'TenAppOne/django_relative_urls.html')


@login_required()
def django_users_view(request):
    return render(request, 'TenAppOne/django_users.html')


@login_required()
def django_user_login_logout_view(request):
    return render(request, 'TenAppOne/django_user_login_logout.html')


@login_required()
def django_ecryption_and_validation_view(request):
    return render(request, 'TenAppOne/django_encryption_and_validation.html')


@login_required()
def django_deployment_view(request):
    return render(request, 'TenAppOne/django_deployment.html')


@login_required()
def django_cbvs_view(request):
    return render(request, 'TenAppOne/django_class_based_views.html')


def git_basics_view(request):
    return render(request, 'TenAppOne/git_basics.html')


def git_advanced_view(request):
    return render(request, 'TenAppOne/git_advanced.html')


def python_view(request):
    return render(request, 'TenAppOne/python.html')


@login_required()
def jquery_basics_view(request):
    return render(request, 'TenAppOne/jquery_basics.html')


def sql_basics_view(request):
    return render(request, 'TenAppOne/sql_basics.html')


def vim_basics_view(request):
    return render(request, 'TenAppOne/vim_basics.html')


def regex_reference_view(request):
    return render(request, 'TenAppOne/regex_reference.html')


@login_required()
def interview_prep_view(request):
    return render(request, 'TenAppOne/interview_prep.html')


@login_required()
def nodejs_intro_and_install(request):
    return render(request, 'TenAppOne/nodejs_intro_and_install.html')


# @login_required()
# def nodejs_global_variables(request):
#     return render(request, 'TenAppOne/nodejs_global_variables.html')


@login_required()
def nodejs_express(request):
    return render(request, 'TenAppOne/nodejs_express.html')


@login_required()
def react_and_django(request):
    return render(request, 'TenAppOne/react_and_django.html')


@login_required()
def react_basics(request):
    return render(request, 'TenAppOne/react_basics.html')


@login_required()
def react_examples(request):
    return render(request, 'TenAppOne/react_examples.html')


@login_required()
def typescript_intro(request):
    return render(request, 'TenAppOne/typescript_intro_and_install.html')


@login_required()
def typescript_reference(request):
    return render(request, 'TenAppOne/typescript_reference.html')