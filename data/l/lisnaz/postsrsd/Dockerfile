## -*- docker-image-name: lisnaz/postsrsd -*-  
#  
# Dockerfile for PostSRSd  
#  
FROM lisnaz/alpine:latest  
MAINTAINER Vincent Gu <g@v-io.co>  
  
# variable list  
ENV APP_DIR /srv/postsrsd  
ENV PROC1 postsrsd -e  
  
ENV SRS_DOMAIN example.com  
ENV SRS_SECRET ${APP_DIR}/postsrsd.secret  
  
# install software stack  
RUN set -ex && \  
DEP=postsrsd && \  
apk add --update --no-cache $DEP && \  
rm -rf /var/cache/apk/* && \  
ln -s /etc/postsrsd /srv/postsrsd  
  
# add runtime scripts  
ADD scripts ${PROC_SCRIPTS_DIR}/  
  
# define default directory  
WORKDIR $APP_DIR  

