from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Poll, Choice
from .forms import PollForm, ChoiceFormSet

def poll_create(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        formset = ChoiceFormSet(request.POST, instance=Poll())
        if form.is_valid() and formset.is_valid():
            poll = form.save()
            formset.instance = poll
            formset.save()
            return redirect('poll_list')
    else:
        form = PollForm()
        formset = ChoiceFormSet(instance=Poll())
    return render(request, 'polls/poll_form.html', {
        'form': form,
        'formset': formset,
    })

def poll_update(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == 'POST':
        form = PollForm(request.POST, instance=poll)
        formset = ChoiceFormSet(request.POST, instance=poll)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('poll_list')
    else:
        form = PollForm(instance=poll)
        formset = ChoiceFormSet(instance=poll)
    return render(request, 'polls/poll_form.html', {
        'form': form,
        'formset': formset,
    })

def poll_delete(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == 'POST':
        poll.delete()
        return redirect('poll_list')
    return render(request, 'polls/poll_confirm_delete.html', {'poll': poll})

def vote(request, poll_id):  # Changed from pk to poll_id to match URL pattern
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/poll_detail.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('poll_results', pk=poll.id)

class HomeView(TemplateView):
    template_name = 'polls/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_polls'] = Poll.objects.all()[:5]  # Get 5 latest polls
        return context

class PollListView(ListView):
    model = Poll
    template_name = 'polls/poll_list.html'
    context_object_name = 'polls'

class PollDetailView(DetailView):
    model = Poll
    template_name = 'polls/poll_detail.html'

class PollResultsView(DetailView):
    model = Poll
    template_name = 'polls/poll_results.html'  # Fixed unterminated string