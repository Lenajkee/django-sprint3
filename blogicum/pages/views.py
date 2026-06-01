from django.shortcuts import render  # type: ignore[import-untyped]
from django.http import HttpResponse  # type: ignore[import-untyped]


def about(request) -> HttpResponse:
    """Описание проекта."""
    return render(request, 'pages/about.html')


def rules(request) -> HttpResponse:
    """Правила проекта."""
    return render(request, 'pages/rules.html')
