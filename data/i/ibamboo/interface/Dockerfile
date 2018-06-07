FROM node:alpine as builder  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY ./client/package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY ./client /usr/src/app  
RUN npm run generate  
  
FROM node:alpine  
  
# Metadata  
LABEL maintainer="Parham Alvani <parham.alvani@gmail.com>"  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
RUN mkdir -p /usr/src/app/client/dist  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
COPY \--from=builder /usr/src/app/dist /usr/src/app/client/dist  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
# Entrypoint  
ENTRYPOINT ["node"]  
CMD ["index.js"]  

