FROM node:7.10  
COPY . /www  
WORKDIR /www  
  
ENV NODE_ENV=production  
  
RUN yarn  
RUN yarn global add http-server  
RUN yarn run build:prod  
  
WORKDIR /www/dist  
  
EXPOSE 80  
ENTRYPOINT ["http-server", "-p 80", "-s"]  

