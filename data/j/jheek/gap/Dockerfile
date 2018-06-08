FROM node:latest  
  
RUN npm install -g forever  
  
COPY package.json /gap/package.json  
WORKDIR /gap  
RUN npm install  
  
COPY . /gap  
RUN npm link  
  
EXPOSE 3000  
CMD gap init && forever --workingDir . /usr/local/bin/gap up

