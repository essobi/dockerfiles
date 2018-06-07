FROM joengenduvel/docker-x11-client  
  
# Developer tools  
RUN apk add --no-cache git nodejs nodejs-npm ruby ruby-dev python2 make gcc
g++ gnupg bzip2 openjdk8  
RUN gem install sass --no-doc  
RUN npm install -g gulp bower polymer-cli --unsafe-perm generator-polymer-
init-custom-build grunt-cli  
  
WORKDIR /root  

