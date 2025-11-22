from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question
from .forms import VoteForm
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import F

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'
    pk_url_kwarg = 'question_id'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'
    pk_url_kwarg = 'question_id'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'
    pk_url_kwarg = 'question_id'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = VoteForm(request.POST)
    if form.is_valid():
        submitted_choice_id = form.cleaned_data.get('choice')
        selected_choice = get_object_or_404(
            question.choices.all(), # type: ignore
            pk = submitted_choice_id
        )
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) # type: ignore
    else:
        return render(request, 'detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice.',
        })
