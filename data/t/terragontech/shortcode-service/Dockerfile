FROM terragontech/node:6.9  
MAINTAINER Terragon Engineering Team <oodigie@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir -p production/app  
  
WORKDIR /production  
  
ADD package.json /production/package.json  
  
ADD run.sh /production/run.sh  
  
ADD app /production/app  
  
RUN npm install && npm cache clean  
  
EXPOSE 8083  
CMD ./run.sh  
  

