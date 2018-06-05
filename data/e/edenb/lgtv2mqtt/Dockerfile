FROM node:slim  
  
# Create a source folder for the app  
RUN mkdir /src  
WORKDIR /src  
  
# Get latest version of the lgtv2mqtt app  
# --strip 1 removes the container folder  
RUN curl -sSL https://github.com/hobbyquaker/lgtv2mqtt/tarball/master | tar
-xvz --strip 1  
  
# Install dependencies  
RUN npm install  
  
# Start app  
CMD node index.js --verbosity=$lgtv2mqtt_v \--name=$lgtv2mqtt_n
\--url=$lgtv2mqtt_u \--tv=$lgtv2mqtt_t  

