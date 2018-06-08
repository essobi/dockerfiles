FROM alpine:3.7  
MAINTAINER paladintyrion <paladintyrion@gmail>  
  
ENV MYSQL_LOG /app/mysql/log  
COPY my.cnf /etc/my.cnf  
  
RUN apk update \  
&& apk add --no-cache bash tzdata \  
&& rm -f /etc/localtime \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& mkdir -p /run/mysqld ${MYSQL_LOG} \  
&& apk add --no-cache mysql mysql-client \  
&& mysql_install_db --user=root > /dev/null \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /app/mysql  
VOLUME ["/var/lib/mysql", "/app/mysql/log"]  
EXPOSE 3306  
CMD ["mysqld", "--user=root"]  

