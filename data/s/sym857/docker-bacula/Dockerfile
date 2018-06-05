# Bacula File Deamon  
FROM centos:centos6  
MAINTAINER sym857  
ENV VERSION_NUMBER 1  
# ENV BACULA_USER nobody  
# ENV BACULA_GRP nobody  
RUN yum install -y bacula-client  
ADD startbacula.sh /startbacula.sh  
RUN chmod +x /startbacula.sh  
  
VOLUME /data  
VOLUME /etc/bacula  
  
#EXPOSE 9101  
EXPOSE 9102  
#EXPOSE 9103  
CMD ["/bin/bash", "-c", "/startbacula.sh"]  

