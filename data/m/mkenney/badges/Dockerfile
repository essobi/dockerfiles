FROM nodesource/node:4.2  
EXPOSE 80  
ENV NODE_ENV production  
VOLUME /var/log  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
  
COPY . /usr/src/app/  
  
CMD ["npm", "start"]  

