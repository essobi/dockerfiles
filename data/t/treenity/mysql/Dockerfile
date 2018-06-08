FROM mysql:5.7  
MAINTAINER Ronan Pozzi <contact@treenity-web.fr>  
  
RUN sed -i -e 's/^bind-address/#bind-address/' /etc/mysql/my.cnf  
  
RUN sed -i -e 's/^max_allowed_packet.*/max_allowed_packet=1073741824/'
/etc/mysql/my.cnf  
  
RUN usermod -u 1000 mysql  
  
RUN chown -R mysql:mysql /var/lib/mysql  
  
EXPOSE 3306  

