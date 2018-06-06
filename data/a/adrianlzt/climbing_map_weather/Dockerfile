# You should always specify a full version here to ensure all of your
developers  
# are running the same version of Node.  
FROM node:8.3.0  
# Override the base log level (info).  
ENV NPM_CONFIG_LOGLEVEL warn  
  
# Install and configure `serve`.  
RUN npm install -g serve  
EXPOSE 5000  
# Default value if not defined this var in docker run  
# This null will imply that internally will use a predefined value hardcoded  
ENV BACKEND_URI null  
  
# Install all dependencies of the current project.  
COPY package.json package.json  
COPY npm-shrinkwrap.json npm-shrinkwrap.json  
RUN npm install  
  
# Copy all local files into the image.  
COPY . .  
  
# Build for production.  
RUN npm run build --production  
  
# Modify endpoint before running  
CMD sed -i "s#window.BACKEND_URI=null#window.BACKEND_URI=${BACKEND_URI}#"
build/index.html && serve -s build  

