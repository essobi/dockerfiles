FROM mustardgrain/java8:latest  
  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
CMD ["/sbin/my_init"]  
  
ENV CASSANDRA_VERSION 3.9  
ENV CASSANDRA_URL
http://www.us.apache.org/dist/cassandra/$CASSANDRA_VERSION/apache-
cassandra-$CASSANDRA_VERSION-bin.tar.gz  
ENV CASSANDRA_HOME /opt/apache-cassandra-$CASSANDRA_VERSION  
  
RUN cd /opt && /usr/bin/curl -L -s $CASSANDRA_URL | tar xz  
  
RUN \  
apt-get update && apt-get install -y \  
python-dev \  
python-setuptools \  
sysstat && \  
easy_install pip  
  
COPY . /src  
  
RUN cp /src/cassandra.yaml $CASSANDRA_HOME/conf  
  
RUN \  
mkdir -p /etc/service/cassandra && cp /src/cassandra-run
/etc/service/cassandra/run  
  
WORKDIR $CASSANDRA_HOME  
  
EXPOSE 7000 7001 7199 9042 9160  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

