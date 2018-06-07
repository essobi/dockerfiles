FROM vanagandr42/baseimage-oraclejdk:5  
# Package version  
ARG HAMBISYNC_VER="1.0-beta"  
# Environment settings  
ARG DEBIAN_FRONTEND="noninteractive"  
# Declare volumes  
VOLUME ["/config", \  
"/app"]  
  
# Add local files  
COPY rootfs/ /  
  
WORKDIR /opt/hambisync/bin  
  
# Expose port of the webservice  
EXPOSE 4567/tcp

