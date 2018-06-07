#FROM node:0.12  
FROM node:6.11  
MAINTAINER Javier Ailbirt <jailbirt@interactar.com>  
ENV destDir /src/theeye-agent  
# Create app directory  
RUN mkdir -p ${destDir}  
# Install Supervisor  
RUN npm install -g supervisor  
# Google API  
RUN npm install googleapis@27 --save  
#Set working Directory  
WORKDIR ${destDir}  
# Bundle app source  
COPY . ${destDir}  
# Install app dependencies  
RUN cd ${destDir}; npm install  
#Fix Permissions.  
RUN mkdir ${destDir}/.tmp  
RUN chmod -R 1777 ${destDir}/.tmp  
# Bundle app source  
#No Port Exposition actually need it. EXPOSE 6080  
#Env variables.  
#By default run prod, If development is requiered This command would be
overriden by docker-compose up  
CMD [ "/src/theeye-agent/run.sh" ]  

