# AUTHOR: João Ribeiro <jonnybgod@gmail.com>  
# DESCRIPTION: jonnybgod/topbeat  
FROM frolvlad/alpine-glibc:alpine-3.3_glibc-2.23  
MAINTAINER João Ribeiro <jonnybgod@gmail.com>  
  
# Here we use several hacks collected from
https://github.com/gliderlabs/docker-alpine/issues/11:  
# # 1. install GLibc (which is not the cleanest solution at all)  
ENV VERSION=1.1.2 PLATFORM=x86_64  
ENV FILENAME=topbeat-${VERSION}-${PLATFORM}.tar.gz  
  
# Environment variables  
ENV TOPBEAT_HOME /opt/topbeat-${VERSION}-${PLATFORM}  
ENV PATH $PATH:${TOPBEAT_HOME}  
  
WORKDIR /opt/  
  
RUN wget -q -O - http://download.elastic.co/beats/topbeat/${FILENAME} | tar xz
-C .  
  
ADD topbeat.yml ${TOPBEAT_HOME}/  
ADD docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["start"]

