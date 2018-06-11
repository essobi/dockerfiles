# uhoh app server  
#  
# VERSION 0.0.1  
#Long Term Supported Ubuntu  
FROM ubuntu:14.04  
MAINTAINER Steve Kallestad  
  
RUN export LC_ALL=C  
RUN apt-get -y update #get the latest package list  
  
#install nodejs and related packages  
RUN apt-get install -y nodejs npm wget  
  
RUN mkdir -p /opt/uhoh  
WORKDIR /opt/uhoh  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install http https mongodb express body-parser assert path jade
passport passport-saml method-override errorhandler mongoose winston
nodemailer  
  
RUN wget https://github.com/su-as/uhoh-services/archive/0.9.tar.gz -O
uhoh.tar.gz  
RUN tar --strip-components=1 -xvzf uhoh.tar.gz  
  
RUN npm install -g node-inspector  
  
EXPOSE 22 3000 3030 5859  
CMD ["/usr/bin/node", "/opt/uhoh/index.js"]  

