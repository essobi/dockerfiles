FROM yesoreyeram/graphite-base:latest  
MAINTAINER Sriramajeyam Sugumaran <yesoreyeram@gmail.com>  
  
RUN apt-get -y update  
RUN apt-get install curl --yes  
RUN apt-get install nginx --yes  
RUN apt-get install gunicorn --yes  
RUN apt-get install supervisor --yes  
  
RUN cp /opt/graphite/conf/carbon.conf.example /opt/graphite/conf/carbon.conf  
RUN cp /opt/graphite/conf/storage-schemas.conf.example
/opt/graphite/conf/storage-schemas.conf  
  
RUN cp /opt/graphite/webapp/graphite/local_settings.py.example
/opt/graphite/webapp/graphite/local_settings.py  
RUN PYTHONPATH=/opt/graphite/webapp/ django-admin migrate
--settings=graphite.settings --run-syncdb  
  
RUN cp /opt/graphite/conf/graphite.wsgi.example /opt/graphite/webapp/wsgi.py  
  
RUN chown -R www-data:www-data /opt/graphite/  
  
WORKDIR /etc/nginx/sites-available/  
RUN curl -O https://raw.githubusercontent.com/yesoreyeram/graphite-nginx-
uwsgi/graphite-nginx-gunicorn/nginx/graphite  
RUN ln -s /etc/nginx/sites-available/graphite /etc/nginx/sites-
enabled/graphite  
  
RUN service nginx stop  
WORKDIR /etc/supervisor/conf.d/  
RUN curl -O https://raw.githubusercontent.com/yesoreyeram/graphite-nginx-
uwsgi/graphite-nginx-gunicorn/supervisor/supervisord.conf  
  
WORKDIR /opt/graphite  
EXPOSE 80 8888 5000 8080  
CMD ["/usr/bin/supervisord"]  

