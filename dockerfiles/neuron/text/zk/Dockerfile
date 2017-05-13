#
# Zookeeper Dockerfile
#
FROM neuron/base-java

# Install zookeeper
RUN wget -q -O - http://apache.mirrors.pair.com/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz | tar -xzf - -C /opt

# Setup env.
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64
ENV ZOO_LOG4J_PROP INFO,CONSOLE,ROLLINGFILE

# Expose ports.
EXPOSE 2181 2888 3888
# Run zookeeper
CMD sh -c "sed -i -e '/server\.$MY_ID=/c\server\.$MY_ID=$(hostname -i):2888:3888' /var/lib/zookeeper/zoo.cfg && /opt/zookeeper-3.4.6/bin/zkServer.sh start-foreground /var/lib/zookeeper/zoo.cfg"
