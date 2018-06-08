# docker build -t medialon/jiraslacknotifier:2.3.0 -t
medialon/jiraslacknotifier:latest .  
#use a tiny node image  
FROM node  
  
#create an app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# install typescript  
# RUN npm install typescript -g  
#use the directory  
WORKDIR /usr/src/app  
  
#copy the sources  
COPY . /usr/src/app  
  
#install NPM modules  
RUN npm install  
  
#compile typescript  
# RUN tsc  
#expose port (could you env to change port)  
EXPOSE 1337  
#start the server  
CMD [ "node", "server.js" ]  
  
# for test  
#CMD ["/bin/bash"]  
# docker push medialon/jiraslacknotifier:latest  
# docker push medialon/jiraslacknotifier:2.3.0  

