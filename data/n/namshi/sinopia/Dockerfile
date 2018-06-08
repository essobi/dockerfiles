FROM node:0.12  
MAINTAINER Oluwaseun Obajobi <oluwaseun.obajobi@namshi.com>  
RUN mkdir -p /opt/sinopia/storage  
WORKDIR /opt/sinopia  
  
ENV SINOPIA_VERSION 1.4.0  
RUN npm install js-yaml sinopia@${SINOPIA_VERSION}  
ADD config.yaml /opt/sinopia/config.yaml  
RUN npm cache clean  
VOLUME /opt/sinopia  
EXPOSE 4873  
CMD ["/opt/sinopia/node_modules/sinopia/bin/sinopia" , "-c",
"/opt/sinopia/config.yaml"]  

