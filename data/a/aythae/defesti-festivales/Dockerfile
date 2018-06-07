# Reference https://nodejs.org/en/docs/guides/nodejs-docker-webapp/  
FROM node:boron-alpine  
MAINTAINER AythaE <aythae@GMail.com>  
  
# Update container packages  
RUN apk update && apk upgrade  
  
# Add user defesti to group wheel and login into it  
# Reference https://github.com/nodejs/docker-
node/blob/master/docs/BestPractices.md#non-root-user  
RUN adduser -S -g wheel defesti  
USER defesti  
  
# Create app directory  
RUN mkdir -p /home/defesti/festivales  
WORKDIR /home/defesti/festivales  
  
# Install app dependencies  
COPY package.json /home/defesti/festivales  
RUN npm install  
  
  
# To Bundle app source  
# COPY . /home/defesti/festivales  
# to expose the port 8080 you need to have it mapped by the docker daemon  
# EXPOSE 8080  
# to choose which command run when the container is running  
CMD [ "npm", "start" ]  

