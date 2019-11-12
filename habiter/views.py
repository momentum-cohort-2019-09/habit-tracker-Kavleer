from django.shortcuts import render

# Create your views here.

def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'home.html', {
        'habits': habits,
    })