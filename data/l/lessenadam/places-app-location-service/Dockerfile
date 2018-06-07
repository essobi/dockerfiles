FROM node:6.2.2  
# create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
#install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install -q  
  
# bundle app source  
COPY . /usr/src/app  
  
EXPOSE 3333  
CMD ["npm", "run", "prod"]  

