FROM node:boron  
  
MAINTAINER jamesrichford@googlemail.com  
  
# Create build directory  
RUN mkdir -p /jamesrichford.com/build  
WORKDIR /jamesrichford.com/build  
  
# Install build dependencies  
COPY package.json /jamesrichford.com/build  
RUN npm install  
  
# Build the app  
COPY . /jamesrichford.com/build  
RUN npm run build  
RUN rm -rf /jamesrichford.com/build/dist/cache-bust-mapping  
RUN rm -rf /jamesrichford.com/build/server/**.ts  
  
# Create app directory  
RUN mkdir -p /jamesrichford.com/app  
WORKDIR /jamesrichford.com/app  
  
# Install app dependencies  
COPY package.json /jamesrichford.com/app  
RUN npm install --production  
  
# Copy assets over  
RUN cp -R /jamesrichford.com/build/dist /jamesrichford.com/app/dist  
RUN cp -R /jamesrichford.com/build/server /jamesrichford.com/app/server  
  
# Tidy up  
RUN rm -rf /jamesrichford.com/build  
  
# Fire up the app  
EXPOSE 8080  
CMD [ "npm", "start" ]  

