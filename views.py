# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from braces.views import LoginRequiredMixin

from .models import DirectoryUser

class DirectoryListView(LoginRequiredMixin, ListView):
    model = DirectoryUser
    context_object_name = 'directoryList'


class DirectoryDetailView(LoginRequiredMixin, DetailView):
    model = DirectoryUser
    context_object_name = 'directoryUser'


class DirectoryCreateView(LoginRequiredMixin, CreateView):
    model = DirectoryUser
    fields = ['user', 'phoneExt', 'room', 'subject']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(DirectoryCreateView, self).form_valid(form)


class DirectoryUpdateView(LoginRequiredMixin, UpdateView):
    model = DirectoryUser
    fields = ['user', 'phoneExt', 'room', 'subject']


class DirectoryDeleteView(LoginRequiredMixin, DeleteView):
    model = DirectoryUser
    success_url = reverse_lazy('directory:list')


