FROM monostream/nodejs-gulp-bower  
  
RUN npm install -g sympm  
  
# Set default volume for image  
# This would be overrided by docker-compose for updatable source code between
development  
COPY . /data  
WORKDIR /data

