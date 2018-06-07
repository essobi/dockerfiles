FROM debian:jessie  
  
RUN apt-get update && apt-get install -y python3 pypy supervisor python-pip
nginx vim  
  
# install uwsgi  
RUN apt-get install -y python-dev  
RUN pip install uwsgi  
  
# Install requirements  
ADD requirements.txt opt/lanets/  
ADD docs-requirements.txt opt/lanets/  
ADD tox.ini opt/lanets/  
ADD docs opt/lanets/  
RUN pip install tox  
RUN pip install -r opt/lanets/requirements.txt  
  
# Add the django app  
ADD manage.py opt/lanets/manage.py  
ADD lanets opt/lanets/lanets  
RUN cd /opt/lanets && python manage.py syncdb --noinput  
  
ADD docker/etc /etc  
ADD docker/opt /opt  
  
# Setup permissions  
RUN chgrp -R www-data /opt/lanets  
RUN chmod -R 770 /opt/lanets  
  
CMD ["/usr/bin/supervisord -c /etc/supervisor/dev.conf"]  
  

