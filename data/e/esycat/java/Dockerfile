FROM esycat/ubuntu:latest  
  
MAINTAINER "Eugene Janusov" <esycat@gmail.com>  
  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_HOME /usr/lib/jvm/java-${JAVA_VERSION_MAJOR}-oracle  
# Auto-accept license agreement  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
  
# Add WebUpd8 PPA and install JRE/JDK, then clean up  
RUN add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
apt-get -qy install oracle-java${JAVA_VERSION_MAJOR}-installer && \  
apt-get clean && \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/archive/* /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-{jre,jdk}*-installer  

