FROM node:8.9-alpine  
ENV NODE_ENV production  
WORKDIR /usr/src/app  
LABEL Jesus Bossa <jesusbossa@protonmail.com>  
COPY package.json .  
RUN npm install --production --silent && mv node_modules ../  
COPY . .  
EXPOSE 3001  
CMD npm start

