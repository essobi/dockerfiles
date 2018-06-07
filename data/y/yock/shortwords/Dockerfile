FROM node:carbon-stretch  
  
ENV BUILD_HOME /shortwords  
RUN mkdir $BUILD_HOME  
WORKDIR $BUILD_HOME  
  
COPY / $BUILD_HOME  
RUN npm i -g lerna  
  
ENTRYPOINT ["lerna"]  

