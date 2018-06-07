FROM mhart/alpine-node:4  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN apk update && \  
apk add make gcc g++ python git nano && \  
npm install --unsafe-perm --production && \  
apk del make gcc g++ python git  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 8080  
EXPOSE 1883  
CMD [ "npm", "start" ]  

