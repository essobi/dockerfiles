FROM node:7.5.0  
COPY package.json /app/package.json  
RUN cd /app/ && npm i --production  
COPY ./ /app/  
WORKDIR /app/  
  
ENV PORT 80  
ENV NODE_ENV production  
  
EXPOSE 80  
CMD npm start  

