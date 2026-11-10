from django.test import TestCase
from django.urls import reverse

from catalogo.models import Categoria, Libro


class CategoriaViewsTests(TestCase):
	def test_home_shows_main_menu_with_books_and_categories(self):
		response = self.client.get("/")

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Menú principal")
		self.assertContains(response, reverse("libro_list"))
		self.assertContains(response, reverse("categoria_list"))

	def test_categoria_list_shows_categories(self):
		Categoria.objects.create(nombre="Novela", descripcion="Ficción")

		response = self.client.get(reverse("categoria_list"))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "<table>")
		self.assertContains(response, "<th>Nombre</th>", html=True)
		self.assertContains(response, "<th>Descripción</th>", html=True)
		self.assertContains(response, "Novela")
		self.assertContains(response, "Editar")

	def test_categoria_create_saves_category(self):
		response = self.client.post(
			reverse("categoria_create"),
			{"nombre": "Historia", "descripcion": "Historia universal"},
		)

		self.assertRedirects(response, reverse("categoria_list"))
		self.assertTrue(Categoria.objects.filter(nombre="Historia").exists())

	def test_categoria_update_changes_category(self):
		categoria = Categoria.objects.create(nombre="Ciencia")

		response = self.client.post(
			reverse("categoria_update", args=[categoria.pk]),
			{"nombre": "Ciencia ficción", "descripcion": "Novelas"},
		)

		self.assertRedirects(response, reverse("categoria_list"))
		categoria.refresh_from_db()
		self.assertEqual(categoria.nombre, "Ciencia ficción")

	def test_categoria_delete_removes_category(self):
		categoria = Categoria.objects.create(nombre="Temporal")

		response = self.client.post(
			reverse("categoria_delete", args=[categoria.pk]),
		)

		self.assertRedirects(response, reverse("categoria_list"))
		self.assertFalse(Categoria.objects.filter(pk=categoria.pk).exists())

	def test_libro_list_displays_books(self):
		categoria = Categoria.objects.create(nombre="Novela")
		Libro.objects.create(
			titulo="Don Quijote",
			autor="Miguel de Cervantes",
			fecha_publicacion="1605-01-16",
			categoria=categoria,
		)

		response = self.client.get(reverse("libro_list"))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Don Quijote")
		self.assertContains(response, "Miguel de Cervantes")
		self.assertContains(response, "Registrar nuevo libro")

	def test_libro_create_displays_form(self):
		Categoria.objects.create(nombre="Novela")

		response = self.client.get(reverse("create_libro"))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Registrar nuevo libro")
		self.assertContains(response, "ISBN")
		self.assertContains(response, "Novela")

	def test_libro_form_prompts_to_create_category_when_none_exist(self):
		response = self.client.get(reverse("create_libro"))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No hay categorías para seleccionar")
		self.assertContains(response, reverse("categoria_create"))

	def test_libro_create_saves_isbn_and_category(self):
		categoria = Categoria.objects.create(nombre="Novela")

		response = self.client.post(
			reverse("create_libro"),
			{
				"titulo": "Don Quijote",
				"autor": "Miguel de Cervantes",
				"isbn": "9788424116048",
				"fecha_publicacion": "1605-01-16",
				"categoria": categoria.pk,
			},
		)

		self.assertRedirects(response, reverse("libro_list"))
		libro = Libro.objects.get(titulo="Don Quijote")
		self.assertEqual(libro.isbn, "9788424116048")
		self.assertEqual(libro.categoria, categoria)
