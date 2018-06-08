FROM node:latest  
ENV NODE_ENV=production  
RUN npm i -g http-server  
ADD . /meego/web  
WORKDIR /meego/web  
CMD ["http-server", "-s", "-c-1"]  

