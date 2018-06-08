FROM ubuntu:latest  
MAINTAINER docker@fhb.de  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install oracle-java8-installer -y  
RUN apt-get install oracle-java8-set-default -y  
ADD http://fhb-flight.s3-website-us-
east-1.amazonaws.com/flightdemo-1.0-SNAPSHOT.jar /service.jar  
ENTRYPOINT java -jar /service.jar  
EXPOSE 8080

