FROM node:6.11.3  
MAINTAINER hugo@feedeo.io  
  
# Set app environment variables  
ARG NPM_TOKEN  
ARG NAME  
ENV NAME $NAME  
ARG VERSION  
ENV VERSION $VERSION  
ARG VERSION_COMMIT  
ENV VERSION_COMMIT $VERSION_COMMIT  
ARG VERSION_BUILD_DATE  
ENV VERSION_BUILD_DATE $VERSION_BUILD_DATE  
  
ENV HOME /opt/$NAME  
  
# Prepare app directory  
RUN mkdir -p $HOME  
WORKDIR $HOME  
  
# Install app  
COPY src $HOME/src  
COPY share $HOME/share  
COPY package.json $HOME  
  
# Install app dependencies  
RUN npm install --production  
  
EXPOSE 3000  
CMD [ "npm", "start" ]  

