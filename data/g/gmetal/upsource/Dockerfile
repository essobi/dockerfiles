# Upsource server environment for ubuntu  
# version 0.0.1  
# Start with phusion/baseimage  
FROM phusion/baseimage  
MAINTAINER gmetaxas <gmetaxas@gmail.com>  
CMD ["/sbin/my_init"]  
# Never ask for confirmations  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-
set-selections  
# Update apt  
RUN apt-get update && apt-get -y install python-software-properties bzip2
software-properties-common wget unzip openjdk-7-jdk  
  
# Download and install upsource  
RUN wget http://download.jetbrains.com/upsource/upsource-1.0.12551.zip &&
unzip upsource-1.0.12551.zip && mv Upsource /usr/local/upsource && rm
upsource-1.0.12551.zip  
  
#Export JAVA_HOME and setup hosts  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64  
RUN export PATH=~/bin:$JAVA_HOME/bin:$PATH  
RUN /usr/local/upsource/bin/upsource.sh configure --listen-port 8081  
EXPOSE 8081  
VOLUME ["/usr/local/upsource/conf/data"]  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#Create script to start upsource blocking it (avoid container termination)  
RUN echo "#!/bin/sh" >> /usr/local/upsource/bin/startme.sh && echo
"/usr/local/upsource/bin/upsource.sh start --base-url $1" >>
/usr/local/upsource/bin/startme.sh && echo " while :; do sleep 1000; done" >>
/usr/local/upsource/bin/startme.sh && chmod +x
/usr/local/upsource/bin/startme.sh  
  

