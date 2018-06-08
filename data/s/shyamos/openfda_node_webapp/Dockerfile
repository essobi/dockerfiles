FROM ubuntu:14.04  
MAINTAINER shyamos "shyam.objectstream.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get update --fix-missing  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN apt-get update  
RUN apt-get update --fix-missing  
  
RUN apt-get install -y nodejs  
RUN apt-get install -y git git-core  
RUN npm install -g express sails grunt-cli  
RUN npm install -g bower mocha should assert  
RUN npm install -g forever  
RUN apt-get update --fix-missing  
  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get autoremove -y  
  
ADD ./config/supervisord.conf /etc/supervisor/conf.d/supervisord-nodejs.conf  
  
RUN ln -s /usr/bin/nodejs /usr/local/bin/node  
  
EXPOSE 1337  
WORKDIR /var/www  
  
RUN rm -rf https://github.com/shyamrock/openFDAWebApp.git; true  
RUN git clone https://github.com/shyamrock/openFDAWebApp.git  
  
WORKDIR /var/www/openFDAWebApp  
  
RUN npm install  
  
# Set environment variables  
ENV TIMEOUT 20000  
VOLUME ["/var/files", "/var/www"]  
  
CMD ["/usr/bin/supervisord", "-n"]  
  

