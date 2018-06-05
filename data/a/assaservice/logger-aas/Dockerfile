#Well well well... it seems like we have some documentation here!  
#Steps to follow:  
# 1) Start MongoDB docker container like such: docker run -p
172.17.0.1:27017:27017 --name some-mongo --restart unless-stopped -d mongo
--auth  
# 2) Type "docker exec -it some-mongo mongo admin" and then create an Admin
user with a password and stuff like suggested in this post:
https://stackoverflow.com/a/29472184  
# 3) Create a logger container like indicated here: docker run -p
127.0.0.1:8001:8001 --link some-mongo --name=logger --restart unless-stopped
-e DATABASE='mongodb://user:password@some-mongo:27017' -d assaservice/logger-
user  
# 4) Enjoy loggin awesome stuff. It's really important to do it, otherwise you
need to start again the previous commands, which may lead to a long iteration
until the enjoyment happens. Please contact your shrink if it does not happen
shortly.  
FROM node:8.9.0  
MAINTAINER Axel Amigo <adamigo@neversyn.com>  
  
#Define the environment variables  
ENV SERVER_PORT=8001  
ENV DATABASE=mongodb://user:password@ds231313.mlab.com:44244/logger-aas  
  
#Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
#Install the sexy dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source (this is not a sexy process)  
COPY . /usr/src/app  
  
EXPOSE ${SERVER_PORT}  
  
CMD [ "npm", "run", "watch" ]  

