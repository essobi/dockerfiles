FROM swapnillinux/cloudera-hadoop-base  
  
MAINTAINER Swapnil Jain <swapnil@linux.com>  
LABEL description="Cloudera Hadoop 5.9 Datanode Docker Image"  
  
RUN mkdir -p /hdfs/data  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
EXPOSE 50020 50075 8042  
VOLUME /hdfs  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

