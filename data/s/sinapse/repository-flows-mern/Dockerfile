FROM node:boron  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app  
RUN npm install  
RUN npm install react-textarea-autosize  
COPY . /usr/src/app  
  
ENV NODE_ENV production  
  
EXPOSE 8000  
CMD ["npm", "start"]  

