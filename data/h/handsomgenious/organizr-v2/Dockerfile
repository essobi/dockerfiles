FROM lsiobase/alpine.nginx:3.7  
  
# set label variables  
ARG BUILD_DATE="2018-06-01"  
ARG VCS_REF="3bd735d"  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="organizr" \  
org.label-schema.url="https://organizr.us/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/causefx/organizr/tree/v2-develop"
\  
org.label-schema.schema-version="1.0"  
RUN \  
echo "**** install packages ****" && \  
apk add \--no-cache \  
curl \  
php7-curl \  
php7-ldap \  
php7-pdo_sqlite \  
php7-sqlite3 \  
php7-session \  
php7-zip  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 80  
VOLUME /config  

