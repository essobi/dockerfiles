# Run retroframes  
FROM node:8.9-alpine  
LABEL maintainer="michel@micheldebree.nl"  
RUN apk upgrade -U \  
&& apk add ca-certificates ffmpeg \  
&& rm -rf /var/cache/*  
WORKDIR /data  
COPY . /retroframes/  
RUN cd /retroframes && npm install  
ENTRYPOINT ["node", "/retroframes/index.js"]  

