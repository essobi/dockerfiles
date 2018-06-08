FROM debian:jessie  
MAINTAINER Giuseppe Pantanetti <gpantanetti@fub.it>  
  
RUN apt-get update && apt-get -y upgrade  
  
# Install NGiNX  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends \  
python uwsgi uwsgi-plugin-python nginx supervisor python-pip  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Configure the uwsgi website  
RUN mv /var/www/html /var/www/project  
COPY uwsgi_params.conf /var/www/project/uwsgi_params  
COPY django_nginx.conf /etc/nginx/sites-available/default  
COPY uwsgi.ini /var/www/project/  
RUN touch /var/www/project/reload  
  
# Install a simple Django website  
COPY requirements.txt /var/www/project/  
RUN pip install virtualenv  
RUN virtualenv --no-site-packages /var/www/project/env  
ENV PATH /var/www/project/env/bin:$PATH  
RUN pip install -r /var/www/project/requirements.txt  
  
RUN mkdir /var/www/project/django  
RUN django-admin startproject project /var/www/project/django  
VOLUME ["/var/www/project/django"]  
  
EXPOSE 80  
# Configure supervisord  
COPY nginx_uwsgi_supervisord.conf /etc/supervisor/conf.d/nginx_uwsgi.conf  
CMD ["/usr/bin/supervisord"]  

