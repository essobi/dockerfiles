FROM ubuntu:latest  
MAINTAINER Julio Monroy <jmonroyq@gmail.com>  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections && \  
apt-get update && \  
apt-get install -y software-properties-common unzip && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean && \  
cd /opt && \  
wget http://downloads.typesafe.com/typesafe-activator/1.3.5/typesafe-
activator-1.3.5.zip && \  
unzip typesafe-activator-1.3.5.zip && \  
rm -f /opt/typesafe-activator-1.3.5.zip && \  
mv /opt/activator-dist-1.3.5 /opt/activator  
  
CMD ["/bin/bash"]  
  

