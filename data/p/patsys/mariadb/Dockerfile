FROM patsys/alpine-mybase  
MAINTAINER Patrick Weber <pat.weber91@gmail.com>  
COPY 25_mariadb_setup.sh /etc/my_init.d/  
COPY 80_mariadb_start.sh /etc/my_init.d/  
RUN chmod u+x /etc/my_init.d/25_mariadb_setup.sh  
RUN chmod u+x /etc/my_init.d/80_mariadb_start.sh  
RUN apk update && apk upgrade && apk add mysql mysql-client && rm -rf
/var/cache/apk/*  
RUN mkdir -p /run/mysqld  
RUN chown mysql:mysql /run/mysqld  
VOLUME ["/var/lib/mysql"]  
CMD ["/etc/start"]  

