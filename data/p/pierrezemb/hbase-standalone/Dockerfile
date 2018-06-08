FROM openjdk:8  
RUN apt-get update  
RUN apt-get -y install supervisor python-pip  
RUN pip install supervisor-stdout  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENV VERSION hbase-2.0.0-beta-1  
ENV DESTINATION /opt/hbase  
  
ADD http://archive.apache.org/dist/hbase/${VERSION}/${VERSION}-bin.tar.gz /  
RUN tar -xvf ${VERSION}-bin.tar.gz  
RUN mv /${VERSION} ${DESTINATION}  
ADD hbase-site.xml /${DESTINATION}/conf/hbase-site.xml  
  
# Folder for data  
RUN mkdir -p /data/hbase  
RUN mkdir -p /data/zookeeper  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV PATH $PATH:/${DESTINATION}/bin  
  
# REST API  
EXPOSE 8080  
# Thrift API  
EXPOSE 9090  
# Zookeeper port  
EXPOSE 2181  
# Master port  
EXPOSE 16000  
# Master info port  
EXPOSE 16010  
# Regionserver port  
EXPOSE 16020  
# Regionserver info port  
EXPOSE 16030  
VOLUME /data/hbase  
VOLUME /data/zookeeper  
WORKDIR ${DESTINATION}  
  
CMD ["/usr/bin/supervisord"]

