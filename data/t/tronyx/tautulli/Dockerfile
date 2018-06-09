FROM lsiobase/alpine.python:3.6  
MAINTAINER christronyxyocum  
  
# Set version label  
ARG BUILD_DATE  
ARG VERSION  
  
# Install packages  
RUN \  
apk add --no-cache --virtual=build-dependencies \  
g++ \  
gcc \  
make \  
python-dev && \  
  
# Install Python modules  
pip install --no-cache-dir -U \  
pycryptodomex plexapi && \  
  
# Install app  
git clone -b master --depth 1 https://github.com/Tautulli/Tautulli /app/plexpy
&& \  
  
# Cleanup  
apk del --purge \  
build-dependencies && \  
rm -rf \  
/root/.cache  
  
# Add local files  
COPY root/ /  
  
# Ports and volumes  
VOLUME /config /logs  
EXPOSE 8181  

