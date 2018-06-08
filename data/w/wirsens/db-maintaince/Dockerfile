FROM node:6-alpine  
ENV NODE_ENV production  
COPY ["package.json", "npm-shrinkwrap.json*", "./"]  
RUN npm install --production --silent  
COPY . .  
CMD npm start

