FROM node:latest  
  
# Bundle app source  
COPY . app/  
WORKDIR app/  
  
# Install app dependencies  
RUN npm install  
  
RUN npm run publish  
  
EXPOSE 8080  
CMD [ "npm", "run", "postbuild" ]  

