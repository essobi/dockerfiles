FROM nginx  
MAINTAINER James Diprose "j.diprose@auckland.ac.nz"  
# Install curl (used to install nodejs) and build-essential (for compiling
native nodejs libraries)  
RUN apt-get update -qq  
RUN apt-get install -qqy curl build-essential  
  
# Install nodejs and update npm to latest version  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
#RUN npm install -g npm  
# Install angular-cli  
RUN npm install -g @angular/cli  
  
# Copies all files and maintains directory structure  
COPY / /research-hub-web/  
  
# Build research hub with angular-cli  
WORKDIR /research-hub-web/  
RUN npm install  
RUN ng build  
  
# Configure nginx  
RUN cp -a ./dist/. /usr/share/nginx/www/  
RUN cp nginx.conf /etc/nginx/nginx.conf  

