from django.shortcuts import render, redirect
from django.db.models import Sum, FloatField
from .models import Widget
from .forms import WidgetForm


def index(request):
    widgets = Widget.objects.all()
    widget_sum = Widget.objects.aggregate(s=Sum("quantity"))
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form, "widget_sum": widget_sum})

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('index')

def delete_widget(request, id):
    widget = Widget.objects.get(id=id)
    widget.delete()
    return redirect('index')