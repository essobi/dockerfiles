FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y binutils  
  
# Install node.js  
RUN cd ~ && \  
apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_7.x -o nodesource_setup.sh && \  
bash nodesource_setup.sh && \  
apt-get install -y nodejs build-essential  
  
# Install uglify-js 3.0.4  
RUN npm install -g uglify-js@3.0.4  
  
# Create the file containing the javascript to uglify  
RUN echo 'function boomBaby(s) { return s.split(/[\\\\\\\/]/); };' >
/tmp/original_javascript.js  
  
# Show the uglifyjs version and the result of uglifying
/tmp/original_javascript.js when starting a container for review  
CMD printf 'uglifyjs -V: ' && \  
uglifyjs -V && \  
printf 'original javascript: ' && \  
cat /tmp/original_javascript.js && \  
printf 'uglified javascript: ' && \  
uglifyjs /tmp/original_javascript.js && \  
/bin/bash  

