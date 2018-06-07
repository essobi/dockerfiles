FROM eviles/alpine-sshd  
  
ARG MYSQL_UID=997  
ARG MYSQL_GID=995  
  
RUN mkdir -m 755 /var/lib/mysql \  
&& chown ${MYSQL_UID}:${MYSQL_GID} /var/lib/mysql  
  
VOLUME /var/lib/mysql  

