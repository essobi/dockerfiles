FROM node:alpine  
LABEL maintainer="nenjotsu@gmail.com"  
  
# Create app directory  
RUN mkdir -p /src  
WORKDIR /src  
  
# Bundle app source  
COPY . /src  
  
# Install app dependencies  
# COPY package.json /src/  
RUN yarn install  
RUN yarn build  
  
EXPOSE 8787  
CMD yarn start

