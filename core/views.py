from django.shortcuts import redirect, render

from core.forms import SignupForm
from item.models import FAQ, Feedback, Gallery, NewsUpdates, Stats


# Create your views here.
def Index(request):
    stats = Stats.objects.all()
    gallery = Gallery.objects.all()
    faqs = FAQ.objects.all()
    news = NewsUpdates.objects.all()
    feedback = Feedback.objects.all()

    return render(request, 'core/home.html', {
        'stats': stats,
        'gallery': gallery,
        'faqs': faqs,
        'news': news,
        'feedback': feedback

    })


def Signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/contact/')
    else:
        form = SignupForm()


    return render(request, 'core/signup.html', {
        'form': form
    })


def Contact(request):
    return render(request, 'core/contact.html')


