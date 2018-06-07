FROM debian:jessie  
  
MAINTAINER Arthur <arthur@corenzan.com>  
  
COPY locale.txt /tmp/  
RUN debconf-set-selections /tmp/locale.txt  
  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LC_ALL=en_US.UTF-8 DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install -y --no-install-recommends mysql-server
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN sed -Ei 's@^(bind-address|log)@#&@' /etc/mysql/my.cnf  
  
VOLUME ["/var/lib/mysql", "/etc/mysql"]  
  
EXPOSE 3306  
COPY mysql.sh /usr/bin/  
CMD ["/usr/bin/mysql.sh"]  

