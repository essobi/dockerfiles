FROM mhart/alpine-node  
  
RUN mkdir -p /usr/app  
RUN chmod -R 777 /usr/app  
WORKDIR /usr/app  
  
COPY package.json /usr/app  
RUN npm install  
  
COPY . /usr/app  
EXPOSE 3000  
CMD [ "npm", "start" ]  

