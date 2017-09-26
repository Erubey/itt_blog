>>> from blog.models import Blog
>>> Blog.objects.all()
<QuerySet [<Blog: Beatles Blog>, <Blog: Beatles Blog>, <Blog: New Name>, <Blog: Titulo>, <Blog: Titulo2>, <Blog: Titulo3>]>
>>> Blog.objects.create(name='Titulo4', tagline='Etiqueta4')
<Blog: Titulo4>
>>> Blog.objects.create(name='Titulo5', tagline='Etiqueta5')
<Blog: Titulo5>
>>> Blog.objects.create(name='Titulo6', tagline='Etiqueta6')
<Blog: Titulo6>
>>> Blog.objects.create(name='Titulo7', tagline='Etiqueta7')
<Blog: Titulo7>
>>> ejemplo = Blog(name='Ejemplo', tagline='Orm')>>> ejemplo.save()
>>> ejemplo1 = Blog(name='Ejemplo1', tagline='Orm1')
>>> ejemplo1.save()
>>> ejemplo2 = Blog(name='Ejemplo2', tagline='Orm2')
>>> ejemplo2.save()
>>> ejemplo3 = Blog(name='Ejemplo3', tagline='Orm3')
>>> ejemplo3.save()
>>> ejemplo.name = 'Example'
>>> ejemplo.save()
>>> ejemplo1.name = 'Example1'
>>> ejemplo1.save()
>>> ejemplo2.name = 'Example2'
>>> ejemplo2.save()
>>> ejemplo3.name = 'Example3'
>>> ejemplo3.save()
>>> Blog.objects.all()
<QuerySet [<Blog: Beatles Blog>, <Blog: Beatles Blog>, <Blog: New Name>, <Blog: Titulo>, <Blog: Titulo2>, <Blog: Titulo3>, <Blog: Titulo4>, <Blog: Titulo5>, <Blog: Titulo6>, <Blog: Titulo7>, <Blog: Example>, <Blog: Example1>, <Blog: Example2>, <Blog: Example3>]>
>>> Blog.objects.filter(name__contains='Titulo')
<QuerySet [<Blog: Titulo>, <Blog: Titulo2>, <Blog: Titulo3>, <Blog: Titulo4>, <Blog: Titulo5>, <Blog: Titulo6>, <Blog: Titulo7>]>
>>> Blog.objects.filter(name__contains='Example')
<QuerySet [<Blog: Example>, <Blog: Example1>, <Blog: Example2>, <Blog: Example3>]>


>>> Blog.objects.get(id=1)
<Blog: Beatles Blog>
>>> Blog.objects.get(id=2)
<Blog: Beatles Blog>
>>> Blog.objects.get(id=5)
<Blog: Titulo2>
>>> Blog.objects.get(id=3)
<Blog: New Name>
>>> Blog.objects.get(id=1)
<Blog: Beatles Blog>
>>> for i in blog:
...     print i.name
... 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'Blog' object is not iterable
>>> for i in Blog:
...     print i.name
... 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'ModelBase' object is not iterable
>>> blogs = Blog.objects.all()
>>> for i in blogs:
...     print i.name
... 
Beatles Blog
Beatles Blog
New Name
Titulo
Titulo2
Titulo3
Titulo4
Titulo5
Titulo6
Titulo7
Example
Example1
Example2
Example3
>>> 

