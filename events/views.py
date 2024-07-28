from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Participant
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    Participant.objects.create(event=event, user=request.user)
    send_mail(
        'Confirmação de Inscrição',
        f'Você se inscreveu no evento {event.title}.',
        'from@example.com',
        [request.user.email],
        fail_silently=False,
    )
    return redirect('event_list')
