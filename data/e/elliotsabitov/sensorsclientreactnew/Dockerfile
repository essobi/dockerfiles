FROM node:boron  
  
# Install yarn | It looks like this is already installed.  
# RUN npm install -g yarn  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
#RUN npm install  
RUN yarn  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 3000  
CMD [ "yarn", "start" ]

