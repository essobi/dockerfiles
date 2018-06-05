FROM terragontech/node:6.9  
MAINTAINER Terragon Engineering Team <iidiang@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir -p production/app  
  
WORKDIR /production  
  
ADD package.json /production/package.json  
  
ADD package.json /production/package.json  
  
ADD app /production/app  
  
RUN npm install && npm cache clean  
  
EXPOSE 9090  
CMD ["npm","start"]

