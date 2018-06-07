FROM node:8-alpine  
ENV NODE_PATH src/  
  
RUN mkdir -p /usr/src/app  
WORKDIR /app  
  
COPY package.json /app/package.json  
RUN yarn install  
RUN mv /app/node_modules /node_modules  
  
COPY . /app  
  
CMD ["yarn", "prod"]  

