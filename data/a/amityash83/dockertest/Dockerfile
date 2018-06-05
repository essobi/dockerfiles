######################################  
## Docker file for Oracle JDK 1.7.0_80  
## based on Ubuntu 14.04 LTS  
######################################  
FROM ubuntu:14.04  
MAINTAINER Amit Mishra  
  
RUN apt-get update \  
&& apt-get upgrade -y  
  
RUN apt-get install -y software-properties-common python-software-properties
&& \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java7-installer && \  
apt-get install oracle-java7-set-default && \  
rm -rf /var/cache/oracle-jdk7-installer  
  
ENV JAVA_HOME="/usr/lib/jvm/java-7-oracle/"  
  
CMD ["/bin/bash"]

