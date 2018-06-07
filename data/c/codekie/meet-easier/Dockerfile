FROM node:6-alpine  
MAINTAINER Josua Amann <josua.amann@zumtobelgroup.com>  
  
# Create app directory  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json npm-shrinkwrap.json ./  
COPY ui-react/package.json ui-react/npm-shrinkwrap.json ./ui-react/  
# Use production install for server and make sure that UI-dependencies are
installed  
# as well  
RUN npm install --production && \  
npm run postinstall  
  
# Set environment variable if public URL shall be overriden  
ARG PUBLIC_URL  
  
# Bundle app source  
COPY . .  
  
# Build app  
# Change permissions, to allow everyone to change into the directories and
read files  
# (if the user which runs the container is different than root)  
RUN echo "$PUBLIC_URL" && \  
npm run build && \  
rm -rf /usr/src/app/ui-react/node_modules && \  
chmod -R +r /usr/src/app && \  
find /usr/src/app -type d -exec chmod +x {} \;  
  
EXPOSE 8080  
CMD ["npm", "start"]  

