FROM ubuntu:14.04  
MAINTAINER laurent Thil <lathil.dev@gmail.com>  
# get Curl  
RUN apt-get update && apt-get install -y curl  
# get java 7 jdk  
RUN apt-get install -y openjdk-7-jdk  
  
RUN mkdir /opt/osgi && cd /opt/osgi  
WORKDIR /opt/osgi  
# Install felix distribution  
RUN curl -O
http://archive.apache.org/dist/felix/org.apache.felix.main.distribution-4.2.1.tar.gz
&& \  
tar zxf org.apache.felix.main.distribution-4.2.1.tar.gz && rm
org.apache.felix.main.distribution-4.2.1.tar.gz && \  
mkdir /opt/osgi/felix-framework-4.2.1/load && \  
mkdir -p /var/felix/fileinstall  
  
VOLUME /var/felix  
  
ADD repository.xml /opt/osgi/felix-framework-4.2.1/conf/repository.xml  
ADD load /opt/osgi/felix-framework-4.2.1/load  
ADD launch_felix.sh /opt/osgi/felix-framework-4.2.1/launch_felix.sh  
ADD felix_config /opt/osgi/felix-framework-4.2.1/felix_config  
  
WORKDIR /opt/osgi/felix-framework-4.2.1  
  
#VOLUME /var/felix  
RUN ./launch_felix.sh < felix_config  
  
EXPOSE 8080  
# launch with gogo shell in nointeractive to be able to run in detach mode  
CMD ["java", "-Dgosh.args=--nointeractive", "-jar","bin/felix.jar"]  
  

