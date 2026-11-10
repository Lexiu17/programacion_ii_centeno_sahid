from django.test import TestCase
from django.urls import reverse


class LeadsLikePageTests(TestCase):
    def test_leads_like_page_is_rendered(self):
        response = self.client.get(reverse("tasks:leads_like"))

        self.assertEqual(response.status_code, 200)
<<<<<<< HEAD
        self.assertContains(response, "Ing. Centeno Sahid")
        self.assertContains(response, "Editor creativo")
        self.assertContains(response, "Organiza tus proyectos y tareas")
        self.assertContains(response, "nosequeestudiar.net")
=======
        self.assertContains(response, "Ing Fransisco javier")
        self.assertContains(response, "Editor creativo")
        self.assertContains(response, "Organiza tus proyectos y tareas")
        self.assertContains(response, "patrimoniocultural.gob.ar")
>>>>>>> 378acc3d337ff8c45492e399c5c027a1a1ed2108
