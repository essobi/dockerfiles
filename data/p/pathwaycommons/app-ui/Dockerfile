# Refer to:  
# https://nodejs.org/en/docs/guides/nodejs-docker-webapp/  
# https://github.com/nodejs/docker-node  
# Node.js base image  
FROM node:8  
# Create an unprivileged user w/ home directory  
RUN groupadd appuser \  
&& useradd --gid appuser --shell /bin/bash --create-home appuser  
  
# Create app directory  
RUN mkdir -p /home/appuser/app  
WORKDIR /home/appuser/app  
  
# Bundle app  
COPY . /home/appuser/app  
  
# Install app dependencies  
RUN npm install  
  
# Build project  
RUN npm run clean  
RUN npm run build  
  
# Expose port  
EXPOSE 3000  
# Change ownership of the app to the unprivileged user  
RUN chown appuser:appuser -R /home/appuser/app  
USER appuser  
  
# Run the command that starts the app  
CMD npm start  

