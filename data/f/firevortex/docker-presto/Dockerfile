FROM java:8-jre  
  
ADD https://repo1.maven.org/maven2/com/facebook/presto/presto-
server/0.161/presto-server-0.161.tar.gz presto-server-0.161.tar.gz  
  
RUN apt-get update && \  
apt-get install -yf python && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
tar xf presto-server-0.161.tar.gz && \  
rm presto-server-0.161.tar.gz  
  
WORKDIR presto-server-0.161

