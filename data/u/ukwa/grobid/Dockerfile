  
FROM java:openjdk-7-jdk  
  
MAINTAINER Andrew Jackson "anj@anjackson.net"  
# update packages and install maven  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y vim wget curl git maven  
  
RUN \  
git clone https://github.com/kermitt2/grobid.git && \  
cd grobid && \  
mvn install -DskipTests  
  
WORKDIR grobid/grobid-service  
  
EXPOSE 8080  
ENV JAVA_OPTS -Xmx2g  
  
CMD mvn -Dmaven.test.skip=true jetty:run-war  
  

