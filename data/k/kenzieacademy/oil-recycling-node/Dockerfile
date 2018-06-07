FROM node:carbon  
  
# Create app directory  
WORKDIR /usr/src/app  
  
# add `/usr/src/app/node_modules/.bin` to $PATH  
ENV PATH /usr/src/app/node_modules/.bin:$PATH  
  
# add environment variables  
ARG NODE_ENV  
ENV NODE_ENV $NODE_ENV  
ARG MONGO_HOST  
ENV MONGO_HOST $MONGO_HOST  
ARG SUPER_USER_EMAIL  
ENV SUPER_USER_EMAIL $SUPER_USER_EMAIL  
ARG SUPER_USER_PASSWORD  
ENV SUPER_USER_PASSWORD $SUPER_USER_PASSWORD  
  
  
ADD node/package.json /usr/src/app/package.json  
RUN npm install --silent  
  
ADD ./node/src /usr/src/app/src  
  
EXPOSE 8080  
CMD ["npm", "start"]  

