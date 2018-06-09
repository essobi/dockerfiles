FROM debian:wheezy  
MAINTAINER Kamil Domański <kamil@domanski.co>  
  
RUN apt-get update && apt-get install -y openjdk-7-jdk wget unzip && apt-get
clean all  
  
ENV TDB_VERSION 0.5.2  
RUN wget -q -O /tmp/titan-${TDB_VERSION}.zip
http://s3.thinkaurelius.com/downloads/titan/titan-${TDB_VERSION}-hadoop2.zip
&& \  
unzip /tmp/titan-${TDB_VERSION}.zip -d /opt && \  
rm /tmp/titan-${TDB_VERSION}.zip  
  
ADD entrypoint.sh /  
  
EXPOSE 8182 8184  
ENTRYPOINT ["/entrypoint.sh"]  

