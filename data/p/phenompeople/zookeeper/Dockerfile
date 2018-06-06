#Base image  
FROM phenompeople/centos-sunjre:latest  
LABEL maintainer="rajesh.jonnalagadda@phenompeople.com"  
ARG ZOOKEEPER_VERSION=3.4.12  
ARG ZOOKEEPER_HOME=/usr/local/zookeeper  
EXPOSE 2181 2888 3888  
RUN useradd zookeeper -s /bin/false -u 400 && \  
wget -q -O /tmp/zookeeper.tar.gz http://www-
us.apache.org/dist/zookeeper/stable/zookeeper-${ZOOKEEPER_VERSION}.tar.gz && \  
tar -xzf /tmp/zookeeper.tar.gz -C /usr/local && \  
ln -sf /usr/local/zookeeper-${ZOOKEEPER_VERSION} ${ZOOKEEPER_HOME} && \  
mkdir -p ${ZOOKEEPER_HOME}/logs && \  
touch /usr/local/zookeeper/logs/zookeeper.out && \  
rm -rf /tmp/zookeeper.tar.gz && \  
chown -R zookeeper:zookeeper /usr/local/zookeeper/logs/  
  
ENV ZOOKEEPER_HOME=${ZOOKEEPER_HOME} \  
PATH=$ZOOKEEPER_HOME:$PATH  
  
ADD zoo.cfg ${ZOOKEEPER_HOME}/conf/zoo.cfg  
ADD start-server.sh ${ZOOKEEPER_HOME}/start-server.sh  
USER zookeeper  
ENTRYPOINT ["/usr/local/zookeeper/start-server.sh"]

