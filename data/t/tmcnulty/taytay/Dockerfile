FROM python:3.5-alpine  
  
ADD requirements.txt /  
RUN set -ex \  
&& apk update \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
make \  
libc-dev \  
musl-dev \  
linux-headers \  
postgresql-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
freetype-dev \  
libxslt-dev \  
libxml2-dev \  
zlib-dev \  
&& pyvenv /venv \  
&& LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install -r
/requirements.txt" \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /venv \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .python-rundeps $runDeps \  
&& apk del .build-deps  
RUN mkdir /code/  
WORKDIR /code/  
ADD . /code/  
EXPOSE 8000  
ENV DEBUG=off UWSGI_VIRTUALENV=/venv UWSGI_WSGI_FILE=taytay/wsgi.py
UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=8 UWSGI_HTTP_AUTO_CHUNKED=1
UWSGI_KEEPALIVE=1 UWSGI_HARAKIRI=20  
RUN SECRET_KEY=none /venv/bin/python manage.py collectstatic --noinput  
RUN /venv/bin/pip install ec2-meta-env  
CMD ["/venv/bin/ec2-meta-env", "-e", "local-ipv4", "-e", "local-hostname",
"/venv/bin/uwsgi"]  

