FROM lsiobase/alpine.python:3.7  
# Set python to use utf-8 rather than ascii.  
ENV PYTHONIOENCODING="UTF-8"  
RUN apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/main \  
rsync \  
cdrkit \  
py2-chardet \  
py2-lxml \  
boost-system \  
boost-python  
  
RUN apk add --no-cache --virtual=build-dependencies \  
\--repository http://nl.alpinelinux.org/alpine/edge/main \  
g++ \  
gcc \  
python2-dev \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
libressl-dev  
  
RUN pip install --no-cache-dir -U pip setuptools>=36 lxml  
  
# Make sure to install setuptools version >=36 to avoid a race condition, see:  
# https://github.com/pypa/setuptools/issues/951  
RUN pip install --no-cache-dir urllib3[socks] flexget subliminal kinopoiskpy
python-telegram-bot  
  
# Copy local files.  
COPY etc/ /etc  
RUN chmod -v +x \  
/etc/cont-init.d/* \  
/etc/services.d/*/run  
  
RUN apk del build-dependencies  
  
# Ports and volumes.  
EXPOSE 5050/tcp  
VOLUME /config  
  
WORKDIR /config  

