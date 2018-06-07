FROM node:latest  
COPY . /vue-app  
WORKDIR /vue-app  
RUN npm install  
RUN npm install -g http-server  
EXPOSE 8080  
RUN npm run build  
CMD ["http-server"]  

