FROM node:boron  
LABEL maintainer="Mike Lee <programmablemike@gmail.com>"  
LABEL description="A docker container for an IP block listing service written
\  
in NodeJS"  
ENV NODE_ENV=production  
COPY ./packages /usr/local/src/brickwall/packages  
WORKDIR /usr/local/src/brickwall  
RUN npm install packages/brickwall-blocker --silent --production  
  
EXPOSE 8000  
CMD [ "bash", "-c", "$(npm bin)/brickwall-blocker-server --host 0.0.0.0 --port
8000"]  

