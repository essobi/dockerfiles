FROM node:7.2.0  
MAINTAINER Joe Costanzo "joe@joeco.info"  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
COPY package.json /home/app/  
  
ENV DOCKERIFIED 1  
RUN apt-get -yq update && \  
apt-get -yq install build-essential  
  
# Set in what directory commands will run  
WORKDIR /home/app  
  
# Put all our code inside that directory that lives in the container  
ADD . /home/app  
  
RUN npm rebuild node-sass && \  
npm install -g gulp bower  
  
# Install dependencies  
RUN npm install && \  
bower install --config.interactive=false \--allow-root && \  
npm cache clean  
  
#Build the app  
RUN gulp  
  
EXPOSE 80  
# The command to run our app when the container is run  
CMD ["gulp","serve:dist"]  

