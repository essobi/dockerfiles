FROM nginx  
  
# Install Node.js  
RUN apt-get update && apt-get upgrade && \  
apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
  
RUN apt-get update && apt-get upgrade && \  
apt-get install -y git nodejs  
  
RUN npm -g install npm@latest  
  
# Install Bower & Grunt  
RUN npm install -g bower gulp  
  
COPY html /usr/share/nginx/html  
  
RUN /bin/bash -c 'cd /usr/share/nginx/html && bower install --allow-root'  
  
RUN apt-get purge -y git npm nodejs curl apt-transport-https lsb-release && \  
apt-get autoremove -y && \  
apt-get clean all  
  
RUN rm -rf /usr/lib/node_modules

