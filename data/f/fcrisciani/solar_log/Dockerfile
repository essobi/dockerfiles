FROM node:alpine  
  
# App directory  
WORKDIR /app  
COPY package.json /app  
copy *.js /app/  
RUN npm install  
CMD [ "npm", "start" ]  

