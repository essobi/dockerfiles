FROM phusion/baseimage:0.9.13  
MAINTAINER Wayne Leroux <WayneLeroux@gmail.com>  
  
# Set up base image  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get -y dist-upgrade  
ENV HOME /root  
RUN echo 'LANG="en_EN.UTF-8"' > /etc/default/locale  
CMD ["/sbin/my_init"]  
  
# Support SSH  
VOLUME /root/.ssh  
  
# Install Java 7  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java7-installer  
RUN update-java-alternatives -s java-7-oracle  
RUN echo 'export JAVA_HOME="/usr/lib/jvm/java-7-oracle"' >> ~/.bashrc  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN export PATH=$PATH  
  
# Install Stash  
RUN apt-get install -y git  
ENV STASH_VERSION 3.2.4  
RUN wget -P /tmp
http://www.atlassian.com/software/stash/downloads/binary/atlassian-
stash-${STASH_VERSION}.tar.gz  
RUN tar xzf /tmp/atlassian-stash-${STASH_VERSION}.tar.gz -C /opt  
RUN mkdir /etc/service/atlassian-stash-${STASH_VERSION} && echo
"#!/bin/bash\n/opt/atlassian-stash-${STASH_VERSION}/bin/start-stash.sh -fg" >
/etc/service/atlassian-stash-${STASH_VERSION}/run && chmod +x
/etc/service/atlassian-stash-${STASH_VERSION}/run  
RUN echo 'export STASH_HOME="/var/stash-home"' >> ~/.bashrc  
ENV STASH_HOME /var/stash-home  
RUN mkdir -p /var/stash-home && chmod 777 /var/stash-home  
VOLUME /var/stash-home  
EXPOSE 7990 7999  
# Install MySQL Support for Stash  
RUN wget -P /tmp http://dev.mysql.com/get/Downloads/Connector-J/mysql-
connector-java-5.1.32.tar.gz  
RUN tar xzf /tmp/mysql-connector-java-5.1.32.tar.gz -C /tmp  
RUN cp /tmp/mysql-connector-java-5.1.32/mysql-connector-java-5.1.32-bin.jar
/opt/atlassian-stash-${STASH_VERSION}/atlassian-stash/WEB-INF/lib/mysql-
connector-java-5.1.32-bin.jar  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

