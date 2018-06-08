FROM google/nodejs  
  
COPY . /  
  
RUN apt-get update && \  
apt-get install -y libicu-dev  
  
RUN npm install && npm install -g forever  
  
ENTRYPOINT forever config.js

