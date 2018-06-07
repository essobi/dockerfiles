FROM ubuntu:16.04  
#  
# expose the grails default port  
#  
EXPOSE 8080  
ARG DEBIAN_FRONTED=noninteractive  
  
RUN apt-get -y upgrade && apt-get -y update && apt-get -y install python-
software-properties && apt-get -y install software-properties-common mysql-
server  
  
RUN ln -snf /bin/bash /bin/sh && apt-get update && apt-get install -y
supervisor git openssh-server && mkdir /data  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
WORKDIR "/data/"  
  
RUN git clone https://github.com/schmalle/honeyalarmg2.git  
  
WORKDIR "/data/honeyalarmg2"  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
#  
# this is only needed to download all needed libraries for grails 2.5.5 (or
newer)  
#  
RUN /data/honeyalarmg2/docker/configdb.sh  
  
RUN ./grailsw war  
  
CMD ["/usr/bin/supervisord"]  
  

