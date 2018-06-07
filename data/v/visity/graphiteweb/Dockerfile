FROM python:2.7  
# Install required packages  
RUN apt-get update && \  
apt-get install -y libcairo2-dev memcached python-cairo sqlite3 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY requirements.txt /tmp/  
RUN pip install -r /tmp/requirements.txt  
# For some reason the default install folder is now no longer at
/opt/graphite. Override.  
RUN pip install --install-option="--prefix=/opt/graphite" graphite-web==0.9.15  
  
# Create users  
RUN addgroup --gid 30100 graphiteweb  
RUN useradd -u 30106 -g graphiteweb -s /bin/false graphiteweb  
  
# Copy configs into place and create needed dirs  
COPY local_settings.py /opt/graphite/webapp/graphite/  
RUN mkdir -p /opt/graphite/storage/log/webapp  
RUN cp /opt/graphite/conf/graphite.wsgi.example
/opt/graphite/webapp/graphite_wsgi.py  
  
# Setup DB for graphite webapp  
RUN export PYTHONPATH=$PYTHONPATH:/opt/graphite/webapp && \  
cd /opt/graphite/webapp/graphite && \  
/usr/local/bin/django-admin.py syncdb --settings=graphite.settings --noinput  
  
# Setup a default NGINX file in case this docker is fronted with NGINX  
RUN mkdir -p /etc/nginx/conf.d  
COPY nginx-graphite.conf /etc/nginx/conf.d/default.conf  
  
COPY docker-entrypoint.sh /  
  
# Default port  
EXPOSE 80  
ENV PYTHONPATH /opt/graphite/webapp  
ENV TERM xterm  
  
# Share volumes when serving via NGINX  
VOLUME /opt/graphite/webapp/content  
VOLUME /etc/nginx/conf.d  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["gunicorn", "--bind=0.0.0.0:80", "graphite_wsgi:application", "--
user=graphiteweb", "--settings=graphite.settings"]  

