FROM alpine:edge  
MAINTAINER Sebastian Knoth <sebastian.knoth@gmail.com>  
  
ENV LANG="en_US.UTF-8" \  
LC_ALL="en_US.UTF-8" \  
LANGUAGE="en_US.UTF-8" \  
DB_USER="admin" \  
DB_PASS="password" \  
TERM="xterm"  
RUN apk -U upgrade && \  
apk --update add \  
mariadb mariadb-client \  
&& \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
COPY /rootfs /  
COPY /scripts /  
  
RUN chmod u+x /run.sh  
  
VOLUME ["/data"]  
EXPOSE 3306  
CMD ["/run.sh"]

