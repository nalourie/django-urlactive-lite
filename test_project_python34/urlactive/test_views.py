from django.shortcuts import render


def a_view(request):
    """first test view function."""
    return render(request, "urlactive/test-template.html")
