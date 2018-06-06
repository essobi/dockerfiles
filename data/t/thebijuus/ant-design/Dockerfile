ARG ANTDESIGN_VERSION=3.5.1  
FROM kkarczmarczyk/node-yarn:8.0-wheezy AS build  
  
ARG ANTDESIGN_VERSION  
  
RUN apt-get -qq update ; apt-get -qq install -y unzip  
  
WORKDIR /antdesign  
  
RUN wget --quiet https://github.com/ant-design/ant-
design/archive/$ANTDESIGN_VERSION.zip  
  
RUN unzip -q $ANTDESIGN_VERSION.zip  
  
WORKDIR /antdesign/ant-design-$ANTDESIGN_VERSION  
  
RUN yarn install  
  
COPY Dockerfile /Dockerfile  

