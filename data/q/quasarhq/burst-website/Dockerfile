FROM node:4-alpine  
ENV NODE_ENV production  
RUN apk --no-cache add git g++ make lftp python zip && \  
npm install -g harp surge && \  
apk del g++ python  
  

