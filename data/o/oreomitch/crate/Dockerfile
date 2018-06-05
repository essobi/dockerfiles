#######################################################################  
# Dockerfile to build Crate.io container image  
# Based on Ubuntu  
#######################################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:12.04  
  
# File Author / Maintainer  
MAINTAINER Mitchell Wong Ho <oreomitch@gmail.com>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise universe" >>
/etc/apt/sources.list  
RUN apt-get update  
  
# Never ask for confirmations  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" |
/usr/bin/debconf-set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" |
/usr/bin/debconf-set-selections  
  
# Add oracle-jdk6 to repositories  
RUN apt-get update  
RUN apt-get install python-software-properties -y  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get install oracle-java7-installer -y  
RUN apt-get install oracle-java7-set-default -y  
  
  
RUN add-apt-repository ppa:crate/stable  
RUN apt-get update  
RUN apt-get install crate -y --force-yes  
  
ENV JAVA_HOME /usr/bin/java  
ENV CRATE_HOME /usr/share/crate  
ENV PATH $CRATE_HOME;$JAVA_HOME;$PATH  
ENV CRATE_CLASSPATH $CRATE_HOME/bin  
EXPOSE 4200  
  
CMD ["/usr/share/crate/bin/crate", "-Des.config=/etc/crate/crate.yml"]  
## END  

