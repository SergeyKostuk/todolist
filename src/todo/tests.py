from django.test import TestCase
from django.urls import reverse
import unittest
from todo.models import DoList


# Create your tests here.

class MyTEsts(TestCase):

    def test_add_new(self):
        url = reverse('add_new')

        self.client.post(url, {'line': 'tetst1',

                               })

        do = DoList.objects.get(id=1)

        self.assertEquals(do.line, 'tetst1')

    def test_del_record(self):
        do = DoList.objects.create(line='1')
        does = DoList.objects.filter()
        self.assertEquals(does.count(), 1)
        url = reverse('remove_record', args=[do.id])
        response = self.client.post(url)
        does = DoList.objects.filter()
        self.assertEquals(does.count(), 0)

    def test_edit_record(self):
        do = DoList.objects.create(line='1')
        url = reverse('edit_record', args=[do.id])
        self.client.post(url, {'line': '2' })
        do = DoList.objects.get(id=1)

        self.assertEquals(do.line, '2')

