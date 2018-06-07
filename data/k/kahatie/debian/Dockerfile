FROM debian:jessie  
MAINTAINER kahatie <kahatie@gmail.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="debian 8" \  
org.label-schema.description="debian 8" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/kahatie/docker" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
# Ne pas poser de questions debconf lors des phases d'installation  
ENV DEBIAN_FRONTEND noninteractive  
# definie le type de terminal (util pour debug et utiliser des editor vi nano
...)  
ENV TERM xterm  
  
# Mise a jour / installation des packet  
RUN apt-get update && apt-get install -y\  
supervisor\  
&& apt-get clean\  
&& rm -rf /var/lib/apt/lists/*  
  
# Copie le fichier de config de supervisord  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Start supervisor  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]  

