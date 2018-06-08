FROM node:8.4.0  
WORKDIR /src  
  
# Install app dependencies  
COPY package.json .  
RUN npm install  
  
COPY public ./public  
COPY src ./src  
  
EXPOSE 3000  
# defined in package.json  
CMD [ "npm", "start"]

