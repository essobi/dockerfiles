FROM terragontech/node:6.2-php  
  
MAINTAINER Terragon Engineering Team <oodigie@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir -p production/app  
  
WORKDIR /production  
  
ADD package.json /production/package.json  
  
ADD app /production/app  
  
RUN npm install && npm cache clean  
  
EXPOSE 9070  
CMD ["npm","start"]  

