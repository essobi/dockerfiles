# Bamboo Server  
#  
# VERSION 0.0.1  
FROM phusion/baseimage:latest  
MAINTAINER Karanbir Singh "krnbr@live.in"  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Environment  
ENV BAMBOO_VERSION 5.15.0.1  
ENV BAMBOO_HOME /home/bamboo  
# Set the BAMBOO_HOST_NAME for setting the hostname  
ENV BAMBOO_HOST_NAME 127.0.0.1  
# Expose web and agent ports  
EXPOSE 8085  
EXPOSE 54663  
ADD server.xml /usr/  
  
# Add runit service  
ADD bamboo-server.sh /etc/service/bamboo-server/run  
RUN chmod +x /etc/service/bamboo-server/run  
ADD docker-cc.sh /bin/  
RUN chmod +x /bin/docker-cc.sh  
  
# Make sure we get latet packages  
RUN apt-get update && apt-get upgrade -y  
  
# Install Java OpenJDK 7, 8 and VCS tools  
RUN apt-get install -yq python-software-properties && add-apt-repository
ppa:webupd8team/java -y && apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -yq oracle-java7-installer git subversion oracle-
java8-installer  
  
RUN mkdir $BAMBOO_HOME  
RUN mkdir /opt/atlassian-bamboo-$BAMBOO_VERSION  
RUN curl -fSL
http://downloads.atlassian.com/software/bamboo/downloads/atlassian-
bamboo-$BAMBOO_VERSION.tar.gz -o /tmp/atlassian-bamboo.tar.gz \  
&& tar -xvf /tmp/atlassian-bamboo.tar.gz -C /opt \  
&& rm /tmp/atlassian-bamboo.tar.gz  
  
# Maven  
RUN mkdir /opt/apache-maven  
RUN curl -fSL
http://redrockdigimark.com/apachemirror//maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz -o maven.tar.gz \  
&& tar -xvf maven.tar.gz -C /opt/apache-maven \  
&& rm maven.tar.gz*  
  
#&& tar -xvf maven.tar.gz -C apache-maven –-strip-components=1 \  
ENV PATH $PATH:/opt/apache-maven/apache-maven-3.3.9/bin:/opt/apache-maven/bin  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

