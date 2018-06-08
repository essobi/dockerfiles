FROM pepechoko/docker-rails  
MAINTAINER pepechoko  
  
## node.js setup  
RUN yum install -y bzip2 freetype fontconfig  
RUN curl -sL https://rpm.nodesource.com/setup | bash -  
RUN yum install -y nodejs  
  
RUN npm install -g bower  
RUN npm install -g grunt-cli  
RUN npm install -g yo  
RUN npm install -g generator-mocha  
RUN npm install -g mocha-phantomjs  
# RUN npm install -g generator-marionette-coffee  
RUN npm install -g generator-marionette  
  

