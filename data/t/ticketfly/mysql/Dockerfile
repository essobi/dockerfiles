FROM mysql:5.6  
MAINTAINER Guillaume Carre "guillaume.carre@ticketfly.com"  
# Allow empty root password  
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes  
  
COPY wait-for-it.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/wait-for-it.sh  
  
COPY my.cnf /etc/mysql/conf.d

