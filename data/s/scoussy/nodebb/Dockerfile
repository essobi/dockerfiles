FROM node:4-alpine  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apk -U add git  
RUN git clone -b v1.x.x https://github.com/NodeBB/NodeBB .  
RUN npm install  
RUN apk del git  
  
ENV NODE_ENV=production \  
daemon=false \  
silent=false  
  
ADD config.sh config.sh  
  
CMD npm start  
  
EXPOSE 4567  

