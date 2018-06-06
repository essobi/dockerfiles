FROM terragontech/node:6.9  
MAINTAINER Terragon Engineering Team <aariyo@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir -p production/app  
  
WORKDIR /production  
  
ADD package.json /production/package.json  
  
ADD app /production/app  
  
RUN npm install && npm cache clean  
  
EXPOSE 8002  
CMD ["npm","start"]  

