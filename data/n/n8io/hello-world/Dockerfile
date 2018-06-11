# Defines the base image for your container. E.g. node, node:0.12.7,
node:0.10.38  
FROM node:4.1.1  
MAINTAINER Nate Clark <nate.clark@ignitionone.com>  
  
# Create a directory to hold your application  
RUN mkdir /app  
  
# Set the $cwd  
WORKDIR /app  
  
# Copy the package.json so we don't retrigger unecessary npm installs  
ADD package.json package.json  
  
# npm install  
RUN npm install  
  
#Add the current directories contents to the container's /app directory  
COPY . .  
  
# Define the default run command. Not actually ran on [docker build].  
# This command is only executed on [docker run].  
CMD ["npm", "run", "start"]

