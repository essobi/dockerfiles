FROM node:7 as webpack  
  
WORKDIR /app  
COPY ./ /app  
RUN npm install  
RUN npm start  
  
FROM debian as hugo  
ADD
https://github.com/spf13/hugo/releases/download/v0.21/hugo_0.21_Linux-64bit.deb
./  
RUN dpkg -i hugo_0.21_Linux-64bit.deb  
WORKDIR /app  
COPY \--from=webpack /app/ ./  
RUN hugo -d ./dist  
  
CMD /bin/bash  
  
FROM nginx  
COPY \--from=hugo /app/dist/ /usr/share/nginx/html/  
  
LABEL traefik.port=80  
EXPOSE 80  

