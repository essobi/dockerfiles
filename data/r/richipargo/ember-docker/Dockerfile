FROM ubuntu:trusty  
  
MAINTAINER Ricardo Tapia Mancera rtapia92@gmail.com  
  
RUN apt-get update && apt-get install -y git curl libgtk2.0-0 libidn11
libglu1-mesa  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get install -y nodejs  
  
RUN npm install -g ember-cli bower phantomjs  

