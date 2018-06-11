FROM alpine:latest  
MAINTAINER yarec<rwtest@gmail.com>  
  
COPY ./entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh \  
&& apk --update add mariadb \  
&& addgroup mysql mysql \  
&& rm -rf /ws/data/mysql \  
&& mkdir -p /ws/data/mysql \  
&& chown -R mysql:mysql /ws/data/mysql \  
&& chown -R mysql:mysql /etc/mysql \  
&& rm -rf /var/cache/apk/*  
  
#VOLUME /ws/data/mysql /ws/log/mysql /ws/mysql/conf /tmp  
EXPOSE 3306  
USER mysql  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "mysqld", "--user=mysql" ]  

