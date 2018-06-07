FROM alpine:3.5  
  
RUN apk add \--update-cache \  
ca-certificates \  
libffi-dev \  
py-pip \  
py-cairo \  
&& rm -rf /var/cache/apk/*  
  
RUN apk add \--update-cache --virtual=build-deps \  
gcc \  
python-dev \  
musl-dev \  
&& apk add \--update-cache nginx \  
&& pip install --upgrade pip && pip install gunicorn \  
&& pip install scandir \  
&& pip install supervisor supervisor-stdout \  
&& pip install https://github.com/graphite-project/graphite-
web/archive/1.0.1.tar.gz \  
&& pip install https://github.com/graphite-
project/whisper/archive/1.0.1.tar.gz \  
&& pip install https://github.com/graphite-project/carbon/archive/1.0.1.tar.gz
\  
&& rm -rf /opt/graphite/conf/*.example \  
&& apk del build-deps \  
&& rm -rf /var/cache/apk/*  
  
COPY scripts /usr/local/bin/  
COPY config /opt/graphite/conf/  
RUN mv /opt/graphite/conf/local_settings.py /opt/graphite/webapp/graphite/ \  
&& mv /opt/graphite/conf/graphite_wsgi.py /opt/graphite/webapp/graphite/ \  
&& mv /opt/graphite/conf/nginx.conf /etc/nginx \  
&& mv /opt/graphite/conf/supervisord.conf /etc/supervisord.conf \  
&& python /usr/local/bin/setup-local-settings.py \  
&& PYTHONPATH=/opt/graphite/webapp django-admin.py collectstatic
--settings=graphite.settings --no-input \  
&& PYTHONPATH=/opt/graphite/webapp django-admin.py makemigrations account
events dashboard url_shortener --settings=graphite.settings \  
&& PYTHONPATH=/opt/graphite/webapp django-admin.py migrate
--settings=graphite.settings  
  
EXPOSE 2003 2004 80  
VOLUME /opt/graphite/storage  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

