FROM node:7-alpine  
  
# Create API directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Copy package file and install dependencies  
COPY package.json /usr/src/app/  
COPY yarn.lock /usr/src/app/  
RUN npm install yarn --silent  
RUN yarn install  
  
# Copy source code  
COPY . /usr/src/app  
RUN yarn build  
RUN yarn global add serve  
  
EXPOSE 5000  
CMD [ "yarn", "serve" ]  

