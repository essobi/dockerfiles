FROM ubuntu:trusty  
  
RUN useradd -s /usr/sbin/nologin -r -M -d /data kudu && \  
mkdir -m 700 -p /data && chown kudu:kudu /data  
  
RUN apt-get update && apt-get -y install wget curl && \  
wget https://archive.cloudera.com/kudu/ubuntu/trusty/amd64/kudu/archive.key -O
archive.key && apt-key add archive.key && \  
wget
'https://archive.cloudera.com/kudu/ubuntu/trusty/amd64/kudu/cloudera.list' -O
/etc/apt/sources.list.d/cloudera.list && \  
apt-get update && apt-get -y dist-upgrade && apt-get -y install kudu kudu-
master kudu-tserver libkuduclient0 libkuduclient-dev  
  
USER kudu  
  
#This will persist data written to /data inside to container to
/var/lib/docker/<somewhere> on the host OS.  
VOLUME /data  
  
COPY startup.sh /  
ENTRYPOINT ["/startup.sh"]  
EXPOSE 7050 7051 8050 8051

