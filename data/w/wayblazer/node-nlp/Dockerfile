FROM node:5.1  
MAINTAINER Ricky Stillwell ricky@wayblazer.com  
  
RUN apt-get update && apt-get install -y supervisor  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
RUN mkdir -p /node /npm /data /logs  
ADD package.json /npm/package.json  
ADD .npmrc /npm/.npmrc  
WORKDIR /npm  
RUN npm install  
  
# environment variables  
ENV NODE_ENV production  
ENV NODE_PATH /npm/node_modules  
  
# volume  
VOLUME ["/data", "/logs" ]  
  
EXPOSE 3000  
CMD ["/usr/bin/supervisord"]  

