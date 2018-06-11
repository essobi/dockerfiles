FROM wolfdeng/alpine:3.6  
MAINTAINER Tony Deng ( wolf.deng@gmail.com )  
  
RUN apk update \  
&& apk add mysql mysql-client pwgen \  
&& rm -rf /var/cache/apk/*  
  
COPY my.cnf /etc/mysql/my.cnf  
COPY entrypoint.sh /entrypoint.sh  
  
EXPOSE 3306  
VOLUME ["/mysql/data", "/mysql/conf", "/mysql/log", "/mysql/run"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
RUN ["chmod","+x","/entrypoint.sh"]  
  
CMD ["/usr/bin/mysqld","--defaults-file=/mysql/conf/mysql/my.cnf","--
user=root","--console","--character-set-server=utf8"]  

