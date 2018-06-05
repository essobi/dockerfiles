FROM node:boron  
  
MAINTAINER Tomasz Netczuk  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv D101F7899D41F3C3  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install yarn && apt-get clean  

