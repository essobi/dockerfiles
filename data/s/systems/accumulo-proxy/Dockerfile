FROM sequenceiq/hadoop-docker  
  
MAINTAINER @systems <systems@vlex.com>  
  
USER root  
  
ENV PATH $PATH:$HADOOP_PREFIX/bin  
  
RUN chown -R root:root $HADOOP_PREFIX  
  
RUN echo -e "\n* soft nofile 65536\n* hard nofile 65536" >>
/etc/security/limits.conf  
  
RUN curl -s
http://mirror.cc.columbia.edu/pub/software/apache/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
| tar -xz -C /usr/local  
RUN ln -s /usr/local/zookeeper-3.4.6 /usr/local/zookeeper;\  
chown -R root:root /usr/local/zookeeper-3.4.6;\  
mkdir -p /var/zookeeper  
ENV ZOOKEEPER_HOME /usr/local/zookeeper  
ENV PATH $PATH:$ZOOKEEPER_HOME/bin  
ADD zookeeper/* $ZOOKEEPER_HOME/conf/  
  
RUN curl -s
http://archive.apache.org/dist/accumulo/1.7.0/accumulo-1.7.0-bin.tar.gz | tar
-xz -C /usr/local  
RUN ln -s /usr/local/accumulo-1.7.0 /usr/local/accumulo;\  
chown -R root:root /usr/local/accumulo-1.7.0  
ENV ACCUMULO_HOME /usr/local/accumulo  
ENV PATH $PATH:$ACCUMULO_HOME/bin  
ADD accumulo/* $ACCUMULO_HOME/conf/  
  
#RUN curl -s http://archive.apache.org/dist/thrift/0.9.3/thrift-0.9.3.tar.gz |
tar -xz -C /usr/local/  
#WORKDIR /usr/local/thrift-0.9.3/lib/py/  
#RUN python setup.py install  
RUN sed -e s/useMockInstance=false/useMockInstance=true/ -e
s/TCompactProtocol/TBinaryProtocol/
/usr/local/accumulo-1.7.0/proxy/proxy.properties > /root/proxy.properties  
#RUN echo PYTHONPATH=/usr/local/accumulo/proxy/thrift/gen-
py/:/usr/lib/python2.6/site-packages python
/usr/local/accumulo-1.7.0/proxy/examples/python/TestClient.py >
/root/testthrift.sh  
ADD *-all.sh /etc/  
RUN chown root:root /etc/*-all.sh;\  
chmod 700 /etc/*-all.sh  
  
ADD start-proxy.sh /etc/  
RUN chown root:root /etc/start-proxy.sh;\  
chmod 700 /etc/start-proxy.sh  
  
ADD init-accumulo.sh /tmp/  
RUN /tmp/init-accumulo.sh  
  
EXPOSE 42424  
CMD /usr/local/accumulo-1.7.0/bin/accumulo proxy -p /root/proxy.properties  

