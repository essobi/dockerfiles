FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y python-pip supervisor=3.0r1-1 gunicorn=19.0-1 nginx-
light=1.6.2-5+deb8u4 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
COPY requirements.txt /srv/requirements.txt  
  
RUN pip install -r /srv/requirements.txt  
  
COPY __init__.py /srv/__init__.py  
COPY manage.py /srv/manage.py  
COPY static /srv/static  
COPY templates /srv/templates  
COPY project /srv/project  
  
COPY supervisord.conf /etc/supervisord.conf  
COPY nginx.conf /etc/nginx/nginx.conf  
  
WORKDIR /srv  
CMD supervisord -c /etc/supervisord.conf  
  
EXPOSE 80  

