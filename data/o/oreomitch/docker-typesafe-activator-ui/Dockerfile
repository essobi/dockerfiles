###############################################  
# Dockerfile to build TypeSafe Activator container image  
# Based on Ubuntu:14.04  
###############################################  
  
# Set the base image to Ubuntu:14.04  
FROM ubuntu:14.04  
  
# File Author / Maintainer  
MAINTANER Mitchell Wong Ho <oreomitch@gmail.com>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty universe" >>
/etc/apt/sources.list  
RUN apt-get update  
  
# Install and start Runit  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y runit  
CMD /usr/sbin/runsvdir-start  
  
# NFS  
# RUN DEBIAN_FRONTEND=noninteractive apt-get install nfs-kernel-server  
  
# Never ask for confirmation  
ENV DEBIAN_FRONTEND noninteractive  
  
# Add oracle-jdk7 to repositories  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java7-installer && \  
apt-get install -y oracle-java7-set-default -y  
  
ENV JAVA_HOME /usr/bin/java  
ENV PATH $JAVA_HOME:$PATH  
  
#Install Activator  
RUN apt-get install -y unzip  
RUN pwd  
RUN wget --progress=dot:giga http://downloads.typesafe.com/typesafe-
activator/1.2.7/typesafe-activator-1.2.7.zip && \  
mv typesafe-activator*.zip /home/ && \  
cd /home && \  
unzip typesafe*.zip && \  
rm typesafe*.zip && \  
ln -s /home/activator-1.2.7 /home/activator-latest  
RUN cd /home/activator-latest/  
  
# Configure Activator  
ENV HOME /home  
WORKDIR /home  
RUN ls -al ~/  
RUN mkdir ~/.activator  
RUN echo '-Dhttp.nonProxyHost="localhost|127.0.0.1"' >>
~/.activator/activatorconfig.txt  
# Run activator  
RUN ls -al  
  
  
VOLUME ["/home/activator-latest"]  
EXPOSE 8888 9000  
CMD ["/home/activator-latest/activator","ui","-Dhttp.address=127.0.0.1"]  
## END  

