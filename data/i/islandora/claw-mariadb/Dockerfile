FROM islandora/claw-base  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
MAINTAINER Nick Ruest <ruestn@gmail.com>  
  
LABEL "License"="MIT" \  
"Version"="0.0.1"  
  
EXPOSE 3306  
ENV MYSQL_ROOT_USER=root  
  
RUN apk-install mariadb mysql-client && \  
cleanup  
  
COPY rootfs /  

