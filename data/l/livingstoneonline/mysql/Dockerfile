FROM livingstoneonline/base:alpine  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="GPLv3" \  
"Version"="0.0.1"  
  
EXPOSE 3306  
ENV MYSQL_ROOT_USER=root  
  
RUN apk-install mariadb mysql-client && \  
cleanup  
  
COPY rootfs /  

