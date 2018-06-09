# Django-gunicorn-nginx  
FROM python:3.4  
MAINTAINER Julien Maupetit <julien@tailordev.fr>  
  
ENV PYTHONUNBUFFERED 1  
# Create running app user  
RUN useradd --create-home django  
RUN mkdir /home/django/app && \  
chown django:django /home/django/app  
VOLUME ["/home/django/app"]  
  
# Install nginx, supervisor & gettext  
RUN apt-get update && \  
apt-get install -y --no-install-recommends gettext nginx supervisor && \  
rm -rf /var/lib/apt/lists/*  
  
# Setup nginx  
RUN rm -fr /etc/nginx/sites-enabled/* && \  
rm -fr /etc/nginx/sites-available/*  
COPY conf/nginx/django /etc/nginx/sites-available/django  
RUN ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled/django  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
VOLUME ["/etc/nginx/sites-available"]  
  
# Setup supervisor  
COPY conf/supervisor/django.conf /etc/supervisor/conf.d/django.conf  
VOLUME ["/etc/supervisor/conf.d"]  
  
# Add gunicorn config  
RUN mkdir /home/django/run && \  
chown django:django /home/django/run  
RUN mkdir -p /usr/local/etc/gunicorn  
COPY conf/gunicorn/django.py /usr/local/etc/gunicorn/django.py  
VOLUME ["/usr/local/etc/gunicorn"]  
  
# Install gunicorn & django project dependencies  
RUN pip install gunicorn  
ONBUILD COPY . /home/django/app/  
WORKDIR /home/django/app  
ONBUILD RUN pip install -r requirements.txt  
  
EXPOSE 80  
ENV PROJECT_NAME foo  
  
CMD ["supervisord", "-n"]  

