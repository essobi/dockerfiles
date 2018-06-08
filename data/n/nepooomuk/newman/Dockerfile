FROM debian:jessie  
MAINTAINER Robin N. Mai <robin.nepomuk.mai@me.com>  
RUN apt-get update -y && apt-get upgrade -y  
RUN apt-get install apt-utils -y  
RUN apt-get install curl -y  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install --yes nodejs  
RUN npm install -g newman@beta  
  
EXPOSE 80 443  

