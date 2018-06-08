FROM ubuntu:16.04  
MAINTAINER Gourav Nema <mail@gourav.info>  
RUN apt-get update && apt-get -y install curl  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
RUN mkdir -p /home/application  
  
COPY ./application /home/application  
WORKDIR "/home/application"  
RUN cd /home/application && npm install  
  
CMD ["npm", "start"]  
  
EXPOSE 8900  

