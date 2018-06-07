FROM node:alpine  
  
# Bundle app source  
COPY . app/  
WORKDIR app/  
  
# Install app dependencies  
RUN npm install  
  
RUN npm run build  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

