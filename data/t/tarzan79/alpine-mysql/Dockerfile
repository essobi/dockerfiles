############################################################  
# Dockerfile to build mysql server container images  
# Based on ARM distrib for Raspberry  
############################################################  
  
  
FROM tarzan79/alpine-base:latest  
MAINTAINER Philip Van <phucvd.ce@gmail.com>  
  
COPY ./startup.sh /  
  
RUN chmod +x /startup.sh \  
&& apk --update add mariadb \  
&& addgroup mysql mysql \  
&& rm -rf /var/lib/mysql \  
&& mkdir -p /var/lib/mysql \  
&& chown -R mysql:mysql /var/lib/mysql \  
&& chown -R mysql:mysql /etc/mysql/ \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /var/lib/mysql /var/log/mysql /etc/mysql/ /tmp  
  
EXPOSE 3306  
USER mysql  
  
ENTRYPOINT [ "/startup.sh" ]  
CMD [ "mysqld", "--user=mysql" ]

