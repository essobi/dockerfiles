FROM node:8.9-alpine  
ENV NODE_ENV development  
WORKDIR /usr/src/app  
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]  
RUN npm install --silent && mv node_modules ../  
COPY . .  
EXPOSE 6100  
CMD npm start

