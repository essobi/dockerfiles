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
  
#Cluster health check for HAproxy  
ADD clustercheck.sh /etc/mysql/clustercheck.sh  
RUN mkdir /etc/service/mariadbhealth  
ADD mariadbhealth.sh /etc/service/mariadbhealth/run  
ADD go_cron.sh /etc/service/gocron/run  
ADD backup.sh /etc/service/gocron/backup.sh  
ADD ./restore.sh /usr/local/bin/s3restore.sh  
RUN chmod 755 /etc/service/mariadb/run && chmod 755 /etc/mysql/clustercheck.sh
&& \  
chmod a+x /usr/local/bin/s3restore.sh && chmod 755
/etc/service/mariadbhealth/run && \  
chmod 755 /etc/service/gocron/*  
  
expose 3306 4567 4568 4444 9200  
CMD ["/sbin/my_init"]

