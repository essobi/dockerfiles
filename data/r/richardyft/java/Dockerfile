FROM ubuntu:14.04  
MAINTAINER Richard Tsai "richard1221@gmail.com"  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \  
apt-get update && apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y  
  
RUN apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-java8-installer && \  
rm -rf /tmp/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
CMD ["bash"]  

