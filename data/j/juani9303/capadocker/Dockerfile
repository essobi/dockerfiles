FROM ubuntu  
RUN apt-get update  
RUN apt-get install -y git  
RUN apt-get install -y maven  
RUN apt-get install -y openjdk-8-jdk  
#RUN git clone https://github.com/juanicallemachado/capaDocker  
RUN mkdir capaDocker  
ADD pom.xml capaDocker/pom.xml  
ADD src capaDocker/src  
RUN mkdir data  
WORKDIR /capaDocker  
EXPOSE 8080  
ENTRYPOINT mvn jetty:run  

