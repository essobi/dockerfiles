# Use 'node' image.  
FROM node:argon  
  
# Create the directory '/usr/src/app'.  
RUN mkdir -p /usr/src/app/  
  
# Make '/usr/src/app' the working directory.  
WORKDIR /usr/src/app/  
  
# Copy the 'package.json' needed by NPM in the current directory to the
'WORKDIR' of the container.  
COPY package.json /usr/src/app/  
  
# Run the basic command to install node and it's dependancy.  
RUN npm install  
  
# Copy the content of the current dir (and sub-dir) to the container's
'WORKDIR'.  
COPY . /usr/src/app  
  
# Expose the port 3000 which is used by the container.  
EXPOSE 3000  
# Specify the command to execute to start the container.  
ENTRYPOINT [ "npm", "start" ]  
CMD []  

