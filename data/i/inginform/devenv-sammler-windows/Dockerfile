FROM suchja/wine:latest  
MAINTAINER Jan Suchotzki <jan@inginform.de>  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.6.2  
ENV DOCKER_MACHINE_VERSION 0.2.0  
ENV BOOT2DOCKER_VERSION 1.6.2  
ENV MSYSGIT_VERSION 1.9.5-preview20150319  
ENV VBOX_VERSION 4.3.28  
ENV VBOX_REVISION 100309  
# Curl ist im Baseimage, aber nicht ca-certificate  
USER root  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /data/  
  
# Laden der für die Installationsroutine benötigten Komponenten  
COPY pakete-laden.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/pakete-laden.sh  
  
WORKDIR /data  
  
USER xclient  
  
CMD ["pakete-laden.sh"]  

