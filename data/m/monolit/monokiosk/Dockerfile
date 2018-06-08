FROM node:argon  
MAINTAINER Jens Peter Secher <jp@openmono.com>  
RUN mkdir -p /usr/src/kiosk  
WORKDIR /usr/src/kiosk  
COPY package.json /usr/src/kiosk/  
COPY setup-production-env.sh /usr/src/kiosk/  
RUN ./setup-production-env.sh  
COPY . /usr/src/kiosk  
RUN ./setup-node-env.sh  
EXPOSE 3000  
CMD [ "npm", "start" ]  

