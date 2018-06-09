FROM debian:wheezy  
  
FROM openjdk:8  
MAINTAINER joanna.ziobrowska@student.uj.edu.pl  
  
# install Java  
RUN apt-get update && apt-get install -y apt-utils && apt-get update && apt-
get -y upgrade  
RUN apt-get -y install unzip && apt-get -y install wget && apt-get -y install
curl  
  
# install scala  
RUN apt-get install apt-transport-https -y  
RUN apt-get install scala -y  
  
# sbt  
RUN curl -L -o sbt-1.1.1.deb https://dl.bintray.com/sbt/debian/sbt-1.1.1.deb
&& dpkg -i sbt-1.1.1.deb && rm sbt-1.1.1.deb  
RUN apt-get update && apt-get install sbt -y  
  
# download play framework & slick  
RUN wget https://www.lightbend.com/activator/template/bundle/play-slick  
  
# MYSQL  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-client mysql-
server  
  
RUN apt-get update  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY ./build.sbt ./  
RUN sbt update  
  
CMD sbt console  

