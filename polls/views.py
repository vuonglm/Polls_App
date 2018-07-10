# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question, Choice

# Create your views here.
def index(request):
	question_list = Question.objects.all()
	context = {'question_list':question_list}
	return render(request, 'polls/index.html', context)
	
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist.")
	return render(request, 'polls/detail.html', {'question': question})
	
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html',{'question': question})
	
def vote(request, question_id):
	
	#return HttpResponseRedirect(reverse('results', args = (question_id)))
	question = get_object_or_404(Question, pk=question_id)
	
	try:
		select_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html',{
			'question': question,
			'error_message': "You didn't select a choice."})
	else:
		select_choice.votes += 1
		select_choice.save()
		return HttpResponseRedirect(reverse('results', args = (question.id,)))