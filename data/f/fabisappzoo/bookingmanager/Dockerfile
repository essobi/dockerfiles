FROM node:latest  
  
# Create app directory  
WORKDIR /usr/src/app  
  
RUN echo "installing nodemon"  
# use nodemon for development  
RUN npm install --global nodemon  
  
RUN echo "caching node-modules"  
# cache node-modules  
COPY package.json /usr/src/app  
RUN npm install  
  
# Bundle app source  
ADD . /usr/src/app  
  
CMD ["nodemon", "-L"]  

