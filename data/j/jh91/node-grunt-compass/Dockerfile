FROM node  
  
USER root  
  
# npm derrière un proxy  
RUN npm config set registry "http://registry.npmjs.org/"  
# Install Bower & Grunt  
RUN npm install -g bower  
RUN bower update --allow-root && npm install -g grunt-cli  
  
# Install compass  
RUN apt-get update -y \  
&& apt-get install -y ruby ruby-dev build-essential \  
&& gem install compass  
  
# Crate work dir  
RUN mkdir /src  
WORKDIR /src/ressources/build  
  
# Exec  
CMD grunt prod && grunt watch  

