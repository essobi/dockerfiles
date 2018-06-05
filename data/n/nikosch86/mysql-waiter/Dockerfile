FROM node:latest  
  
ENV NODE_ENV=production  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
# COPY yarn.lock /usr/src/app/  
RUN npm install yarn -g  
RUN yarn  
  
COPY . /usr/src/app  
  
EXPOSE 3000  
CMD [ "npm", "start" ]  

