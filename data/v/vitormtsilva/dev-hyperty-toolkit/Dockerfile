FROM node:carbon  
LABEL maintainer=vitor-t-silva@telecom.pt  
  
RUN apt-get update && apt-get install -y vim  
  
RUN mkdir -p /toolkit  
  
# Change the work directory  
WORKDIR /toolkit  
  
ENV PATH=/toolkit/node_modules/.bin:$PATH  
  
# Copy package.json  
COPY package.json /toolkit/  
  
# Install app dependencies  
RUN npm install  
  
# Copy all structure  
COPY . /toolkit/  
  
# Start the gulp server task  
ENTRYPOINT npm run start:dev  
  
# Expose HTTPS Port  
EXPOSE 443  

