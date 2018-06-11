FROM debian:buster-slim  
  
ENV JAVA_HOME /jre  
  
RUN apt-get update && \  
apt-get install wget -y \--no-install-recommends && \  
apt-get clean && \  
wget http://dl.bintray.com/walkingdevs/mirrors/jre-8.102.tar.gz && \  
tar xf jre-8.102.tar.gz && \  
rm jre-8.102.tar.gz && \  
mv jre* jre && \  
ln -s /jre/bin/java /bin  

