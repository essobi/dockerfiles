FROM centos:7  
LABEL description="Zookeeper 3.4.11. \  
\- KUCHEEV A.P. \  
"  
  
RUN yum install -y java-1.8.0-openjdk && \  
yum clean all && \  
rm -rf /var/cache/yum  
  
ADD ./add /  
  
RUN curl -O -J -L http://apache-
mirror.rbc.ru/pub/apache/zookeeper/zookeeper-3.4.10/zookeeper-3.4.10.tar.gz &&
\  
tar -xf /zookeeper-3.4.10.tar.gz && \  
rm -rf /zookeeper-3.4.10.tar.gz; \  
chmod +x /entrypoint.sh && \  
mv /zookeeper-3.4.10 /opt/zookeeper  
  
ENV ZK_DIR="/opt/zookeeper"  
ENV CLIENT_PORT=2181  
ENV TICK_TIME=2000  
ENV INIT_LIMIT=10  
ENV SYNC_LIMIT=5  
ENV NODES_LIST=""  
ENV NODE_ID=""  
CMD ["/entrypoint.sh"]

