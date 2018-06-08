#  
# Ubuntu Java Dockerfile  
FROM phusion/baseimage:0.9.17  
MAINTAINER Tom Ginader <gin.nader94@gmail.com>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list  
RUN apt-get -y update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-
properties software-properties-common  
  
# install Java 8  
ENV JAVA_VER 8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \  
apt-get update && \  
echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1
select true | sudo /usr/bin/debconf-set-selections && \  
apt-get install -y --force-yes --no-install-recommends oracle-
java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default && \  
apt-get clean && \  
rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer  
  
# set oracle as default java  
RUN update-java-alternatives -s java-8-oracle  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc  
  
RUN apt-get install -y git-all  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN git clone https://github.com/gin-nader/MSCS721-roomScheduler.git  
RUN echo "8" | java -jar
MSCS721-roomScheduler/target/RoomScheduler-1.0-SNAPSHOT-jar-with-
dependencies.jar  
  
CMD ["/sbin/my_init"]  

