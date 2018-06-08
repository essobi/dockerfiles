# Sourced from https://github.com/rvernica/docker-library, thanks!  
FROM alpine:3.5  
  
RUN apk add \--update-cache \  
ca-certificates \  
libffi-dev \  
py-cairo \  
py-pip \  
py-twisted \  
py-psycopg2 \  
&& rm -rf /var/cache/apk/*  
  
RUN pip install --upgrade pip \  
&& pip install \  
carbon \  
django \  
django-tagging \  
gunicorn \  
pyparsing \  
pytz \  
whisper \  
&& pip install https://github.com/graphite-project/ceres/tarball/master  
  
RUN apk add \--update-cache --virtual=build-deps \  
gcc \  
python-dev \  
musl-dev \  
&& pip install scandir \  
&& pip install https://github.com/graphite-project/graphite-web/tarball/master
\  
&& apk del build-deps \  
&& rm -rf /var/cache/apk/*  
  
RUN cp /opt/graphite/conf/carbon.conf.example /opt/graphite/conf/carbon.conf \  
&& cp /opt/graphite/conf/storage-schemas.conf.example \  
/opt/graphite/conf/storage-schemas.conf \  
&& cp /opt/graphite/webapp/graphite/local_settings.py.example \  
/opt/graphite/webapp/graphite/local_settings.py \  
&& cp /opt/graphite/conf/graphite.wsgi.example \  
/opt/graphite/webapp/graphite/graphite_wsgi.py  
  
RUN PYTHONPATH=/opt/graphite/webapp django-admin.py \  
collectstatic --settings=graphite.settings --no-input \  
&& PYTHONPATH=/opt/graphite/webapp django-admin.py \  
makemigrations account events dashboard url_shortener \  
\--settings=graphite.settings \  
&& PYTHONPATH=/opt/graphite/webapp django-admin.py \  
migrate --settings=graphite.settings  
  
EXPOSE 2003  
EXPOSE 2004  
EXPOSE 8080  
VOLUME /opt/graphite/static  
  
  
CMD /opt/graphite/bin/carbon-cache.py start \  
&& PYTHONPATH=/opt/graphite/whisper:/opt/graphite/webapp/graphite \  
/usr/bin/gunicorn graphite_wsgi:application --workers 4 \--bind :8080  

