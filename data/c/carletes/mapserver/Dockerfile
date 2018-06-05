FROM bitnami/minideb:jessie  
  
# Use a reliable Debian mirror (https://github.com/rgeissert/http-
redirector/issues/75)  
RUN sed --in-place 's/httpredir.debian.org/ftp.uk.debian.org/'
/etc/apt/sources.list  
  
# Enable `jessie-backports` repositories, so that we get the latest  
# Mapserver from the debian-GIS project.  
#  
# Line stolen from `debian:jessie-backports` Dockerfile.  
RUN awk '$1 ~ "^deb" { $3 = $3 "-backports"; print; exit }'
/etc/apt/sources.list > /etc/apt/sources.list.d/backports.list  
  
# Create Unix user and group to run Mapserver. Give them predictable UIDs and
GUIDs.  
RUN groupadd -g 9001 mapserver && \  
useradd -r -d /home/mapserver -m -g mapserver -u 9001 mapserver  
  
ARG MAPSERVER_VERSION  
  
# Install Mapserver from backports  
RUN install_packages -t jessie-backports \  
cgi-mapserver=$MAPSERVER_VERSION-* \  
mapserver-bin=$MAPSERVER_VERSION-* \  
spawn-fcgi  
  
# Include documentation about this image.  
COPY README.md /README.md  
  
# Startup script.  
COPY scripts/mapserver /mapserver  
RUN chmod 0755 /mapserver  
  
# Volume for MapServer data.  
VOLUME ["/data"]  
  
# User-configurable parameters.  
ENV FCGI_LISTEN_ADDRESS=0.0.0.0 \  
FCGI_LISTEN_PORT=9001 \  
FCGI_NPROC=1 \  
FCGI_BACKLOG=1024 \  
FCGI_UID=mapserver \  
FCGI_GID=mapserver \  
MS_ERRORFILE=stderr  
  
# Image metadata.  
ARG BUILD_DATE  
ARG IMAGE_NAME  
ARG VCS_REF  
ARG VCS_URL  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.description="A FastCGI MapServer instance" \  
org.label-schema.docker.cmd="docker run -v/some/mapserver/data:/data:ro
$IMAGE_NAME" \  
org.label-
schema.docker.params="FCGI_LISTEN_ADDRESS=0.0.0.0,FCGI_LISTEN_PORT=9001,FCGI_NPROC=1,FCGI_BACKLOG=1024,FCGI_UID=mapserver,FCGI_GID=mapserver"
\  
org.label-schema.name="MapServer" \  
org.label-schema.schema-version="1.0.0-rc1" \  
org.label-schema.url="http://mapserver.org/" \  
org.label-schema.usage="/README.md" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL  
  
# On y va!  
CMD ["/mapserver"]  

