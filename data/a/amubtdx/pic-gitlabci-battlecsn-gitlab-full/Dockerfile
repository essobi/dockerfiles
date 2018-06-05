FROM debian:stretch-slim  
  
ENV TOMCAT_MAJOR=8 \  
TOMCAT_VERSION=8.0.44  
RUN bash -c 'mkdir -p /usr/share/man/man{1..8}' && \  
apt-get update && \  
apt-get install -y --no-install-recommends openjdk-8-jdk-headless maven tree
git bzip2 mongodb xsltproc curl && \  
curl -jksSL -o /tmp/apache-tomcat.tar.gz
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz && \  
tar -C /opt -xzf /tmp/apache-tomcat.tar.gz && \  
mv /opt/apache* /opt/tomcat && \  
rm -rf /tmp/* && \  
apt-get clean && \  
rm -rf /usr/share/man/* && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
WORKDIR /opt/tomcat  
  
COPY tomcat-users.xml conf/tomcat-users.xml  
COPY run.sh run.sh  
  
EXPOSE 8080 27017  
CMD [ "./run.sh" ]  

