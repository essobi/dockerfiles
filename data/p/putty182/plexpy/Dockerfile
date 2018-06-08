FROM putty182/ubuntu-base  
MAINTAINER putty182  
  
# set build arg  
ARG DEBIAN_FRONTEND=noninteractive  
  
# install  
RUN git clone \--depth 1 https://github.com/Tautulli/Tautulli \  
/app/plexpy && \  
  
# install pycryptodomex  
pip install --no-cache-dir -U \  
pycryptodomex && \  
  
# clean up  
rm -rf \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
VOLUME /config /logs  
EXPOSE 8181  

