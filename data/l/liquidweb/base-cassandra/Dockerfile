FROM devdb/cassandra:latest  
MAINTAINER Dan Burke <dburke@liquidweb.com>  
  
RUN add-apt-repository ppa:fkrull/deadsnakes -y && apt-get update && apt-get
install python2.7 -y && apt-get clean  
ADD cassandra-run /etc/service/cassandra/run  

