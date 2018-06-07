FROM linuxserver/deluge:latest  
RUN \  
apk update && apk add --no-cache \  
ca-certificates \  
libressl2.5-libssl \  
p7zip \  
unrar \  
unzip && \  
  
apk add --no-cache --virtual=build-dependencies \  
g++ \  
gcc \  
libffi-dev \  
libressl-dev \  
py2-pip \  
python2-dev && \  
  
pip install --no-cache-dir -U \  
incremental \  
pip && \  
pip install --no-cache-dir -U \  
crypto \  
mako \  
markupsafe \  
pyopenssl \  
service_identity \  
six \  
twisted \  
zope.interface  
RUN apk update && apk add --no-cache git ffmpeg  
RUN pip install --no-cache-dir -U requests requests[security] requests-cache
babelfish "guessit<2" "subliminal<2" stevedore python-dateutil deluge-client
qtfaststart gevent  
RUN apk del --purge \  
build-dependencies && \  
rm -rf /root/.cache  

