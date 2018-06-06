FROM ubuntu:14.04  
MAINTAINER Ben Companjen <ben@companjen.name>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get install --no-install-recommends -y maven
openjdk-7-jdk  
RUN adduser --shell /bin/bash --disabled-password dasishuser  
  
USER dasishuser  
ADD . /home/dasishuser  
WORKDIR /home/dasishuser  
  
RUN mvn install  
  
EXPOSE 8080  
CMD ["mvn", "jetty:run"]  

