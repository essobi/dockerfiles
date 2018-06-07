FROM node:4.5  
EXPOSE 3000  
WORKDIR /app  
CMD [ "/bin/bash "]  
  
COPY . /app  
RUN npm install  
RUN npm run build-js  

