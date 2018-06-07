FROM python:3.6-alpine  
  
ADD requirements.txt /requirements.txt  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
make \  
libc-dev \  
musl-dev \  
linux-headers \  
pcre-dev \  
postgresql-dev \  
python3-dev \  
gettext \  
jpeg-dev \  
zlib-dev \  
freetype-dev \  
lcms2-dev \  
openjpeg-dev \  
tiff-dev \  
tk-dev \  
tcl-dev \  
harfbuzz-dev \  
fribidi-dev \  
&& python3.6 -m pip install -U pip \  
&& LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "python3.6 -m pip install --no-cache-
dir -r /requirements.txt" \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /venv \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .python-rundeps $runDeps \  
&& apk del .build-deps  

