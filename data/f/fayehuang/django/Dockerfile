FROM python:3.5  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
RUN apt-get update && apt-get install -y \  
gcc \  
gettext \  
vim \  
postgresql-client libpq-dev \  
apache2 apache2-dev \  
openssh-client openssh-server \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/* && apt-get clean all  
  
COPY requirements.txt /usr/src/app/requirements.txt  
RUN pip install -r /usr/src/app/requirements.txt  
  
# setup wsgi_module  
RUN echo "LoadModule wsgi_module /usr/local/lib/python3.5/site-
packages/mod_wsgi/server/mod_wsgi-py35.cpython-35m-x86_64-linux-gnu.so" >
/etc/apache2/mods-available/wsgi_express.load  
RUN a2enmod wsgi_express  
COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf  
# develop:8080(runserver), production:80(httpd)  
EXPOSE 8080 80  

