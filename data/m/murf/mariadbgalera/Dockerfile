FROM phusion/baseimage:latest  
  
MAINTAINER Mikael@murf.se  
  
ENV HOME /root  
  
COPY build.sh /build.sh  
RUN chmod 755 /build.sh  
RUN /build.sh  
  
# Add config(s) - standalone and cluster mode  
ADD ./my.cnf /etc/mysql/my.cnf  
#Setup startup  
#MariaDB  
RUN mkdir /etc/service/mariadb  
ADD mariadbgalera.sh /etc/service/mariadb/run  
RUN chmod 755 /etc/service/mariadb/run  
  
#Cluster health check for HAproxy  
ADD clustercheck.sh /etc/mysql/clustercheck.sh  
RUN chmod 755 /etc/mysql/clustercheck.sh  
RUN mkdir /etc/service/mariadbhealth  
ADD mariadbhealth.sh /etc/service/mariadbhealth/run  
RUN chmod 755 /etc/service/mariadbhealth/run  
  
expose 3306 4567 4568 4444 9200  
CMD ["/sbin/my_init"]

