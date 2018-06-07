FROM frolvlad/alpine-oraclejdk8:slim  
MAINTAINER Hieu Nguyen <hieu.nguyen@ssosol.com>  
  
ENV HZ_VERSION=3.5 \  
HZ_HOME=/hazelcast \  
HZ_CONFIG=/hazelcast/config.xml  
  
RUN mkdir $HZ_HOME &&\  
wget -P $HZ_HOME
http://repo1.maven.org/maven2/com/hazelcast/hazelcast/$HZ_VERSION/hazelcast-$HZ_VERSION.jar  
  
ADD start.sh $HZ_HOME/  
  
WORKDIR $HZ_HOME  
EXPOSE 5701  
# Start hazelcast standalone server.  
CMD ./start.sh  

