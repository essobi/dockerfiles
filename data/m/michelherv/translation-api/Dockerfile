# specify the node base image with your desired version node:<version>  
FROM node:6  
# replace this with your application's default port  
EXPOSE 3000  
# set the current dir  
WORKDIR /home/node  
  
# copy the files into image  
COPY . .  
  
# download dependencies  
RUN [ "yarn" ]  
  
# start the server  
ENTRYPOINT [ "yarn", "start" ]  

