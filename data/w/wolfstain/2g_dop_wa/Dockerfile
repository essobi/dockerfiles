FROM node:8.10 as build-deps  
WORKDIR /usr/src/app  
COPY package.json yarn.lock ./  
RUN yarn  
COPY . ./  
  
EXPOSE 3006  

