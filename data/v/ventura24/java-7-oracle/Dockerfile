FROM ubuntu:15.10  
MAINTAINER ventura24  
  
ENV JAVA_VER 7  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update  
  
RUN echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1
select true | /usr/bin/debconf-set-selections && \  
apt-get install -y --force-yes --no-install-recommends oracle-
java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default oracle-
java${JAVA_VER}-unlimited-jce-policy  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists && \  
rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer  

