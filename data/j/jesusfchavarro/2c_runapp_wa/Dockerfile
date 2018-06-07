# base image  
FROM node:9.6.1  
# set working directory  
RUN mkdir /runapp_wa  
WORKDIR /runapp_wa  
  
# add `/runapp_wa/node_modules/.bin` to $PATH  
ENV PATH /runapp_wa/node_modules/.bin:$PATH  
  
# install and cache app dependencies  
COPY package.json /runapp_wa/package.json  
RUN npm install --silent  
#RUN npm install react-scripts@1.1.1 -g --silent  
ADD . /runapp_wa  
  
# start app  
CMD ["npm", "start"]

