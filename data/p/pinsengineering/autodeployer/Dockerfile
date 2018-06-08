FROM terragontech/node:6.9  
MAINTAINER Terragon Engineering Team <tech@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir -p production/  
  
WORKDIR /production/  
  
ADD . /production/  
  
EXPOSE 6066  
RUN npm install && npm cache clean  
  
CMD ["npm","start"]  

