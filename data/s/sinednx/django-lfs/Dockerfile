# Django LFS Dockerfile  
FROM ubuntu:14.04  
MAINTAINER Denis Darii <denis.darii@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install python2.7-dev wget -y sqlite3 libjpeg-dev  
RUN wget https://pypi.python.org/packages/source/d/django-lfs/django-lfs-
installer-0.9.0a1.tar.gz && tar xzf django-lfs-installer-0.9.0a1.tar.gz  
WORKDIR /lfs-installer  
RUN /usr/bin/python2.7 bootstrap.py  
RUN bin/buildout -v  
RUN sed --in-place "s/'ENGINE': 'django.db.backends.',/'ENGINE':
'django.db.backends.sqlite3',/" /lfs-installer/lfs_project/settings.py  
RUN sed --in-place "s/'NAME': '',/'NAME': '\/lfs-installer\/lfs_project\/demo-
lfs-db.sqlite3',/" /lfs-installer/lfs_project/settings.py  
# fix a bug in lfs_generate_products command  
RUN sed --in-place "s/path = open(os.path.join(os.path.dirname(__file__),
\"..\", \"utils\", \"data\"))/path = os.path.join(os.path.dirname(__file__),
\"..\", \"utils\", \"data\")/" /lfs-
installer/eggs/django_lfs-0.9.0a1-py2.7.egg/lfs/utils/generator.py  
RUN bin/django syncdb --noinput  
RUN echo "from django.contrib.auth.models import User;
User.objects.create_superuser('admin', 'admin@example.com', 'admin')" |
bin/django shell  
RUN bin/django migrate  
RUN bin/django lfs_init  
RUN bin/django collectstatic --noinput  
RUN bin/django lfs_generate_products  
EXPOSE 8000  
CMD ["bin/django", "runserver", "0.0.0.0:8000"]  

