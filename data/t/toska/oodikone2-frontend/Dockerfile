FROM node:8.9.4  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN npm i  
  
RUN npm run dist  
RUN npm install -g serve  
  
EXPOSE 5000  
CMD ["serve", "-s", "-l", "5000", "dist"]  

