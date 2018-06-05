FROM ubuntu  
  
MAINTAINER Sivabalan  
  
#RUN apk add --update wget curl docker  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-
common  
  
RUN \  
apt-get update && apt-get install -y curl && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ENV AMBRY_VERSION="0.1"  
ADD download-ambry.sh /tmp/download-ambry.sh  
RUN /tmp/download-ambry.sh  
  
VOLUME ["/ambry"]  
  
#RUN root_dir=`ls /opt/ | grep ambry` && echo $root_dir  
#ENV AMBRY_HOME /opt/$root_dir  
#RUN echo $AMBRY_HOME  
ADD start-ambry.sh /usr/bin/start-ambry.sh  
  
# Use "exec" form so that it runs as PID 1 (useful for graceful shutdown)  
CMD ["start-ambry.sh"]  
  
EXPOSE 1174  

