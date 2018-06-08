# # You should always specify a full version here to ensure all of your
developers  
# # are running the same version of Node.  
# FROM node:8.0.0  
  
# # The base node image sets a very verbose log level.  
# ENV NPM_CONFIG_LOGLEVEL warn  
  
# # Copy all local files into the image.  
# COPY . .  
  
# # Build for production.  
# RUN npm rebuild node-sass --force  
# RUN npm run build  
  
# # Install `serve` to run the application.  
# RUN npm install -g serve  
  
# # Set the command to start the node server.  
# CMD serve -s dist  
  
# # Tell Docker about the port we'll run on.  
# EXPOSE 5000  
  
# You should always specify a full version here to ensure all of your
developers  
# are running the same version of Node.  
FROM node:8.0.0  
  
# Override the base log level (info).  
ENV NPM_CONFIG_LOGLEVEL warn  
# Install and configure `serve`.  
RUN npm install -g serve  
CMD serve -s dist  
EXPOSE 5000  
  
# Install all dependencies of the current project.  
COPY package.json package.json  
RUN npm install  
  
# Copy all local files into the image.  
COPY . .  
  
# Build for production.  
RUN npm run build

