FROM node:8-alpine  
  
USER root  
  
RUN npm set progress=false && npm config set depth 0 && npm cache clean
--force  
  
WORKDIR /opt/app  
COPY . .  
  
RUN apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing vips-dev fftw-dev && \  
apk add --no-cache make curl gcc g++ python && \  
npm install && \  
apk del fftw-dev make gcc g++ python && \  
rm -rf /var/cache/apk/*  
RUN npm run build  
RUN npm prune --production  
  
EXPOSE 80  
VOLUME [ "/opt/app/data" ]  
  
CMD [ "npm", "start" ]  

