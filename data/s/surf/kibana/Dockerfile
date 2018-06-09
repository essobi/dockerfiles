# VERSION 0.0.1  
# BUILD-USING: docker build -t kibana .  
# PUSH-USING: docker tag base surf/kibana && docker push surf/kibana  
FROM surf/base-node  
MAINTAINER Dan Kinsley <dan@surfbeta.com>  
  
RUN mkdir /app  
ADD server.js /app/server.js  
ADD package.json /app/package.json  
WORKDIR /app  
RUN curl --silent
https://download.elasticsearch.org/kibana/kibana/kibana-3.1.0.tar.gz --output
kibana.tar.gz  
RUN tar -zxf kibana.tar.gz  
RUN ln -s kibana-3.1.0 kibana  
  
RUN npm install --production  
  
EXPOSE 5000  
CMD ["npm","start"]  

