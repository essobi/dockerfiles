FROM node:8-alpine  
  
WORKDIR /usr/src/app  
  
COPY ["package-lock.json", "package.json", "/usr/src/app/"]  
RUN npm i  
  
COPY . /usr/src/app  
  
EXPOSE 8080  
CMD ["node", "/usr/src/app"]  

