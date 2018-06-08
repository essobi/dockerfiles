FROM ubuntu:latest  
MAINTAINER harit.himanshu@yahoo.in  
RUN apt-get update && \  
apt-get install -y htop && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
echo orable-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get install oracle-java8-set-default && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list && \  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 && \  
apt-get install -y apt-transport-https && \  
apt-get update && \  
apt-get install -y sbt && \  
apt-get install -y python-pip && \  
pip install -U Sphinx  
  
ENTRYPOINT ["/bin/bash"]  
ENV JAVA_HOME="/usr/lib/jvm/java-8-oracle/"  

