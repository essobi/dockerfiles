FROM ruby:2.4.1-stretch  
  
RUN apt-get update && apt-get -y dist-upgrade && apt-get install apt-
transport-https  
  
COPY nodejs.sources.list /etc/apt/sources.list.d  
COPY nodesource.gpg.key /root  
RUN apt-key add /root/nodesource.gpg.key  
  
RUN apt-get update && apt-get -y install nodejs && apt-get -y clean  
RUN npm install yarn -g  

