FROM node:latest  
MAINTAINER Alexey Vakulich "soulSpringg@gmail.com"  
ENV SRC_DIR=/usr/workspace/signal  
  
ADD . $SRC_DIR  
WORKDIR $SRC_DIR  
  
RUN yarn install  
  
CMD ["node", "./bin/signal.js"]  
  
EXPOSE 3334

