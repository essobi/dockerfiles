FROM ubuntu:14.04  
MAINTAINER cesedge  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common  
RUN add-apt-repository ppa:webupd8team/java  
  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 boolean
true" | debconf-set-selections  
  
RUN apt-get update && apt-get install -y oracle-java8-installer  
  
COPY quarksjava-1.1.jar quarksjava-1.1.jar  
CMD ["java", "-jar", "quarksjava-1.1.jar", "CommonApplication"]  

