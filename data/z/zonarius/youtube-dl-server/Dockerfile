FROM node:9-alpine  
EXPOSE 8080  
RUN apk --no-cache add youtube-dl ffmpeg tini ca-certificates  
ENV NODE_ENV production  
COPY package.json package-lock.json /app/  
RUN cd /app && npm i  
COPY dist/ /app/dist/  
ENTRYPOINT ["/sbin/tini", "node", "/app/dist/index.js"]  

