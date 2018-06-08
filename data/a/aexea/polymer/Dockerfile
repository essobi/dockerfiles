FROM ubuntu:14.04  
MAINTAINER Aexea Carpentry  
  
RUN apt-get update && apt-get install -y \  
curl \  
&& apt-get clean  
RUN curl -sL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add -  
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >>
/etc/apt/sources.list.d/google.list  
RUN apt-get update && apt-get install -y \  
xvfb \  
firefox \  
google-chrome-stable \  
nodejs \  
nodejs-legacy \  
npm \  
git \  
default-jre \  
ruby \  
ruby-dev \  
build-essential \  
&& apt-get clean  
  
RUN gem install sass  
RUN gem install sass-css-importer --pre  
RUN npm install -g bower gulp generator-polymer  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN mkdir -p /opt/code  
WORKDIR /opt/code  
  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
  
COPY package.json /opt/code/package.json  
RUN npm install  
COPY bower.json /opt/code/bower.json  
RUN bower install  

