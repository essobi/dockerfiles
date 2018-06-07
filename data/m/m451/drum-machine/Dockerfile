# simple dockerfile for testing automatic builds  
# lets use the node.js base image  
FROM node  
MAINTAINER Robert Szymczak <rszymczak@fum.de>  
  
# copy github source  
RUN mkdir /src  
ADD . /src  
  
# Install dependencies for our web-project  
# install ruby and sass  
RUN apt-get update && apt-get install ruby -y  
RUN gem install sass  
  
# change workdir to /src  
WORKDIR /src  
# install and configure grunt  
RUN npm install  
RUN npm install -g grunt-cli  
RUN npm install -g grunt  
  
# change workdir to /src/publics/assets  
WORKDIR public/assets/  
# install and configure bower  
RUN npm install -g bower  
RUN yes | bower install --allow-root -y  
  
#change workdir to /src  
WORKDIR /src  
  
# let's expose our webapp port to the docker host  
EXPOSE 8080  
# Set a static, non-changeable entrypoint  
ENTRYPOINT ["grunt"]  
#Override parent-image CMD so it dosn't get passed as argument to ENTRYPOINT  
CMD []  

