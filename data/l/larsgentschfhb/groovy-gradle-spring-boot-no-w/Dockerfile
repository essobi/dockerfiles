FROM ubuntu:16.04  
MAINTAINER docker@thb.de  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties  
RUN add-apt-repository ppa:webupd8team/java -y  
  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
RUN apt-get install -y oracle-java8-installer  
RUN update-alternatives --config java  
  
ADD ./build/libs/groovy-gradle-spring-boot-no-war-1.0.jar /service.jar  
  
#ADD https://s3-eu-west-1.amazonaws.com/fhb-deployment/groovy-gradle-spring-
boot-no-war-1.0.jar /service.jar  
EXPOSE 8080  
ENTRYPOINT java -jar /service.jar  

