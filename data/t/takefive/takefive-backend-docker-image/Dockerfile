# Targets latest Ubuntu  
FROM ubuntu:latest  
  
MAINTAINER Xiaohang Yu <xiaohang@takefiveinteractive.com>  
  
ENV THRIFT_VERSION 0.9.2  
ENV GRADLE_VERSION 2.6  
# Upgrade repository manifests  
RUN apt-get update  
  
# Install build essentials  
RUN apt-get install -y build-essential  
  
# Install Git  
RUN apt-get install -y git  
  
# Install Unzip  
RUN apt-get install -y unzip  
  
# Install JDK 8  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& apt-get install -y --no-install-recommends oracle-java8-installer oracle-
java8-set-default \  
&& apt-get autoremove --purge -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/oracle-
jdk8-installer  
  
RUN update-java-alternatives -s java-8-oracle  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV JRE_HOME /usr/lib/jvm/java-8-oracle/jre  
  
# Install gradle  
WORKDIR /usr/bin  
RUN wget https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-
all.zip -O gradle.zip  
RUN unzip gradle.zip  
RUN mv gradle-$GRADLE_VERSION gradle  
ENV PATH $PATH:/usr/bin/gradle/bin  
  
# Install thrift  
RUN mkdir thriftsrc  
WORKDIR thriftsrc  
RUN apt-get update && apt-get install -y --no-install-recommends libboost-dev
libboost-test-dev \  
libboost-program-options-dev libboost-system-dev libboost-filesystem-dev \  
libevent-dev automake libtool flex bison pkg-config g++ libssl-dev  
RUN wget http://www.interior-
dsgn.com/apache/thrift/$THRIFT_VERSION/thrift-$THRIFT_VERSION.tar.gz -O
thrift.tar.gz  
RUN mkdir thrift  
RUN tar xvzf thrift.tar.gz -C ./thrift --strip-components=1  
WORKDIR /usr/bin/thriftsrc/thrift  
RUN ./configure && make  
RUN make install  
WORKDIR /usr/bin  
RUN rm -rf thriftsrc  
  
# Switch to app folder  
WORKDIR $HOME  
RUN mkdir app appdata  
VOLUME $HOME/appdata  

