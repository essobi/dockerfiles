# Version: 0.0.1  
FROM akagelo/jenkins-slave-maven3  
MAINTAINER Oleg Vyukov <gelo@vyukov.ru>  
  
  
  
ENV MYSQL_USER jenkins  
ENV MYSQL_PASS jenkins  
ENV MYSQL_DB jenkins  
  
  
# обновляшки  
RUN apt-get update  
  
#maven из репов debian  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mongodb mysql-server
mysql-client postgresql postgresql-contrib redis-server  
  
#запуск сервисов через через самопальную систему иннициализации  
ADD etc/ /etc/  
  

