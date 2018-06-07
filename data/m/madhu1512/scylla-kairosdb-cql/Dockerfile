FROM scylladb/scylla:2.1.3  
#install nc  
RUN yum install nc -y  
  
#install  
RUN yum install wget -y && \  
wget
https://github.com/kairosdb/kairosdb/releases/download/v1.2.1/kairosdb-1.2.1-1.rpm
&& \  
yum install -y kairosdb-1.2.1-1.rpm && \  
rm -rf kairosdb-1.2.1-1.rpm  
  
ADD supervisor/ /etc/supervisord.conf.d  
ADD kairos-run.sh kairos-run.sh  
RUN chmod +x /kairos-run.sh  

