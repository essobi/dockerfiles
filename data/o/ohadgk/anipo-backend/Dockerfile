# The official nodejs docker image  
FROM node:latest  
  
#Copy package.json only to temp folder, install its dependencies,  
# set workdir and copy the dependnecies there  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /home/app && cp -a /tmp/node_modules /home/app/  
WORKDIR /home/app  
  
# Copy the rest of the files to the container workdir  
ADD . /home/app  
  
# install forever to run the application  
RUN npm install -g forever  
  
EXPOSE 8080 3000  
# The command run our app as forever process as PID 1 (main).  
CMD ["forever", "server.js"]

