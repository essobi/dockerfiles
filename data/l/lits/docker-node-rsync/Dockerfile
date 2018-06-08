FROM node:latest  
RUN sh -c 'echo "deb http://http.us.debian.org/debian/ jessie contrib non-free
main" >> /etc/apt/sources.list' \  
&& apt-get update -qq -y \  
&& apt-get install -qq -y rsync  
  
### install ember CLI and bower ###  
RUN npm install ember-cli -g  
RUN npm install bower -g  

