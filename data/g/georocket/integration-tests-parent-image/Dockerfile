FROM debian:jessie  
MAINTAINER Michel Kraemer <michel.kraemer@igd.fraunhofer.de>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
groovy \  
mongodb-clients \  
s3cmd \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -s
http://www.eu.apache.org/dist/hadoop/common/hadoop-2.7.2/hadoop-2.7.2.tar.gz |
tar -xz -C /usr/local/ \  
&& ln -s /usr/local/hadoop-2.7.2 /usr/local/hadoop  
  
RUN grape install org.apache.commons commons-exec 1.3  
  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/  
  
ADD data /data  

