FROM node:5.10  
RUN apt-get update && apt-get install -y wget openjdk-7-jdk --fix-missing  
  
RUN mkdir /src && npm install nodemon bower gulp-cli -g  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-
amd64-v0.2.0.tar.gz && tar -C /usr/local/bin -xzvf dockerize-linux-
amd64-v0.2.0.tar.gz  
  
COPY ./ /src  
WORKDIR /src  
RUN update-alternatives --config javac  
RUN npm install  
RUN npm run build  
  
EXPOSE 8080  
EXPOSE 3001  
EXPOSE 3000  
EXPOSE 3030  
CMD dockerize -wait http://mongo:27017 -timeout 60s npm run dev  

