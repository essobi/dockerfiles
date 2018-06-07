FROM ubuntu:12.10  
MAINTAINER Brandon Rice <brice84@gmail.com>  
  
RUN apt-get -y install software-properties-common unzip  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get -y install oracle-java7-installer ant && apt-get clean  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-7-oracle" >> /etc/environment  
  
ADD
http://downloads.sourceforge.net/project/pentaho/Data%20Integration/5.0.1-stable/pdi-
ce-5.0.1-stable.zip /  
RUN unzip pdi-ce-5.0.1-stable.zip  
  
WORKDIR /data-integration  
  
EXPOSE 8181  
CMD ["./carte.sh", "0.0.0.0", "8181"]  
  

