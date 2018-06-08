FROM node:0.12.4  
# dependancy  
RUN npm install redis  
RUN npm install getenv  
RUN npm install express  
  
# application src  
COPY htdocs/ /src/htdocs/  
COPY inventoryService.js /src/  
  
# work default directory  
WORKDIR /src/  
  
ENV REDIS_HOST redisdb  
ENV REDIS_PORT 6379  
EXPOSE 80  
# default command on run  
CMD ["node","inventoryService.js"]  
  
RUN npm install express

