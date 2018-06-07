FROM node:7.10.0  
MAINTAINER Team Reelevant <dev@reelevant.com>  
  
ENV DOCKER_USER node  
ENV HOME /home/$DOCKER_USER  
  
# Mongodb tools 3.4  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main"
| tee /etc/apt/sources.list.d/mongodb-org-3.4.list  
RUN apt-get update && apt-get install -y mongodb-org-tools  
WORKDIR $HOME  
  
COPY package.json .  
RUN npm install  
COPY cases cases  
COPY mocks mocks  
COPY helpers helpers  
  
CMD ["npm", "start"]  
  
EXPOSE 80  

