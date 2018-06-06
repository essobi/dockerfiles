FROM alpine  
  
MAINTAINER <support@collectiveacuity.com>  
  
# Update Alpine environment  
RUN apk update  
RUN apk upgrade  
RUN apk add ca-certificates  
  
# Install Java  
RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories  
RUN echo '@community http://nl.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories  
RUN apk update  
RUN apk upgrade  
RUN apk add openjdk8-jre-base@community  
  
# Install Python & Pip  
RUN apk add curl  
RUN apk add python  
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python  
  
# Install Cassandra  
# http://www.apache.org/dyn/closer.lua/cassandra/3.0.15/apache-
cassandra-3.0.15-bin.tar.gz  
RUN wget http://www-us.apache.org/dist/cassandra/3.0.15/apache-
cassandra-3.0.15-bin.tar.gz  
RUN tar -xvzf apache-cassandra-3.0.15-bin.tar.gz  
RUN rm apache-cassandra-3.0.15-bin.tar.gz  
RUN mv apache-cassandra-3.0.15 /home/cassandra  
RUN mkdir /var/lib/cassandra  
RUN mkdir /var/log/cassandra  
  
# Establish Cassandra Environmental Variables  
ENV CASSANDRA_VERSION 3.0.15  
ENV CASSANDRA_HOME /home/cassandra  
ENV PATH $PATH:/home/cassandra/bin  
  
# Install Python3, Pip & Yaml Module  
RUN apk add python3  
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3  
RUN pip3 install pyyaml  
  
# Import Startup Script Files  
COPY ./update.py /update.py  
COPY ./cassandra-default.yaml /cassandra-default.yaml  
COPY ./entry.bash /entry.bash  
RUN mv entry.bash entry.sh  
  
# Expose Cassandra Ports  
# 7000: intra-node communication  
# 7001: TLS intra-node communication  
# 7199: JMX  
# 9042: CQL  
# 9160: thrift service  
EXPOSE 7000 7001 7199 9042 9160  
# Clean APK cache  
RUN rm -rf /var/cache/apk/*  

