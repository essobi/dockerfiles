FROM yesoreyeram/graphite-base:latest  
MAINTAINER Sriramajeyam Sugumaran <yesoreyeram@gmail.com>  
  
RUN apt-get -y update  
RUN apt-get install curl --yes  
RUN apt-get install nginx --yes  
RUN apt-get install uwsgi --yes  
RUN apt-get install uwsgi-plugin-python --yes  
RUN apt-get install supervisor --yes  
  
RUN cp /opt/graphite/conf/carbon.conf.example /opt/graphite/conf/carbon.conf  
RUN cp /opt/graphite/conf/storage-schemas.conf.example
/opt/graphite/conf/storage-schemas.conf  
  
RUN cp /opt/graphite/webapp/graphite/local_settings.py.example
/opt/graphite/webapp/graphite/local_settings.py  
RUN PYTHONPATH=/opt/graphite/webapp/ django-admin migrate
--settings=graphite.settings --run-syncdb  
  
RUN chown -R www-data:www-data /opt/graphite/  
  
RUN cp /opt/graphite/conf/graphite.wsgi.example /opt/graphite/conf/wsgi.py  
WORKDIR /etc/uwsgi/apps-available/  
RUN curl -O https://raw.githubusercontent.com/yesoreyeram/graphite-nginx-
uwsgi/master/uWSGI/graphite  
RUN ln -s /etc/uwsgi/apps-available/graphite /etc/uwsgi/apps-enabled/graphite  
  
WORKDIR /etc/nginx/sites-available/  
RUN curl -O https://raw.githubusercontent.com/yesoreyeram/graphite-nginx-
uwsgi/master/nginx/graphite  
RUN ln -s /etc/nginx/sites-available/graphite /etc/nginx/sites-
enabled/graphite  
  
WORKDIR /etc/supervisor/conf.d/  
RUN curl -O https://raw.githubusercontent.com/yesoreyeram/graphite-nginx-
uwsgi/master/supervisor/supervisord.conf  
  
WORKDIR /opt/graphite  
EXPOSE 80 8888 2003 8080  
CMD ["/usr/bin/supervisord"]  

