FROM debian:jessie  
  
MAINTAINER zhoumingjun <zhoumingjun@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget \  
telnet \  
openjdk-7-jdk \  
supervisor  
  
RUN apt-get clean  
  
# env  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
RUN mkdir -p /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN mkdir /hbase-setup  
WORKDIR /hbase-setup  
  
ADD ./install-hbase.sh /hbase-setup/  
ADD ./hbase-site.xml /hbase-setup/  
  
RUN ./install-hbase.sh  
  
#  
COPY hbase-site.xml /opt/hbase/conf/hbase-site.xml  
  
RUN /opt/hbase/bin/hbase-config.sh  
  
# Zookeeper  
EXPOSE 2181  
# HBase Master Info port  
EXPOSE 16010  
# HBase Regionserver port  
EXPOSE 16020  
# HBase Regionserver Info port  
EXPOSE 16030  
# HBase REST  
EXPOSE 8080  
# Thrift2  
EXPOSE 9090  
CMD ["/usr/bin/supervisord"]  

