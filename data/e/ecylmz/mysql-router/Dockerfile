FROM debian:jessie  
MAINTAINER Emre Can Yılmaz <emrecan@ecylmz.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq && apt-get install -y curl apparmor && rm -rf
/var/lib/apt/lists/*  
  
RUN curl -fSL -o mysql-router.deb http://dev.mysql.com/get/Downloads/MySQL-
Router/mysql-router_2.0.2-1debian8_amd64.deb  
RUN dpkg -i mysql-router.deb && rm -f mysql-router.deb  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 7001 7002  
CMD ["/usr/sbin/mysqlrouter", "--extra-config=/root/router.ini"]  

