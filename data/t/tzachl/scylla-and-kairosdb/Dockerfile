# Add KairosDB to Scylla Docker image  
FROM scylladb/scylla  
MAINTAINER Tzach Livyatan  
  
#install nc  
RUN yum install nc -y  
  
#install Kairos  
RUN yum install wget -y  
RUN wget
https://github.com/kairosdb/kairosdb/releases/download/v1.1.2/kairosdb-1.1.2-1.rpm  
RUN yum install kairosdb-1.1.2-1.rpm -y  
  
ADD supervisor/ /etc/supervisord.conf.d  
ADD kairos-run.sh kairos-run.sh  
  

