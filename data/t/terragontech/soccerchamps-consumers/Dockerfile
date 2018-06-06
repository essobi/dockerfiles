FROM terragontech/node:6.9  
MAINTAINER Terragon Engineering Team <oodigie@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir -p production/app  
  
WORKDIR /production  
  
ADD package.json /production/package.json  
  
ADD app /production/app  
  
ADD run.sh /production/run.sh  
  
ADD run.sh /production/app/run.sh  
  
RUN chmod +x /production/run.sh  
  
RUN npm install && npm cache clean  
  
CMD ./run.sh  

