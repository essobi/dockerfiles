FROM python:3.5-alpine  
  
RUN set -ex \  
&& apk add --no-cache --update \  
build-base \  
ttf-dejavu \  
gcc \  
make \  
libc-dev \  
musl-dev \  
linux-headers \  
pcre-dev \  
zlib-dev \  
libffi-dev \  
libffi \  
gdk-pixbuf \  
jpeg-dev \  
postgresql-dev \  
python3-dev \  
cairo-dev \  
pango-dev \  
libmagic \  
cairo \  
pango \  
glib \  
git \  
nginx \  
supervisor \  
nodejs \  
&& rm -rf /var/cache/apk/* && \  
chown -R nginx:www-data /var/lib/nginx  
  
RUN pip install uwsgi  
RUN pip install weasyprint  
  
COPY ./requirements.txt /requirements.txt  
RUN pip install --no-cache-dir -r /requirements.txt  
  
COPY ./fonts /usr/share/fonts  
RUN fc-cache  

