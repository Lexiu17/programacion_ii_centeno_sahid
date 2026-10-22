from django.test import TestCase
from django.urls import reverse


class LeadsLikePageTests(TestCase):
    def test_leads_like_page_is_rendered(self):
        response = self.client.get(reverse("tasks:leads_like"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ing Fransisco javier")
        self.assertContains(response, "Editor creativo")
        self.assertContains(response, "Organiza tus proyectos y tareas")
        self.assertContains(response, "patrimoniocultural.gob.ar")
