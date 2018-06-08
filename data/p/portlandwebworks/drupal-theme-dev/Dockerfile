FROM debian:jessie  
MAINTAINER portlandwebworks  
  
# Change our shell  
RUN rm /bin/sh \  
&& ln -s /bin/bash /bin/sh  
  
# Create the mounting directory  
RUN mkdir -p /var/theme  
WORKDIR /var/theme  
  
# Install pre-requisite software  
RUN apt-get update \  
&& apt-get install -y curl \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y build-essential nodejs \  
&& apt-get clean  
  
# Install tooling  
RUN npm install -g nodemon node-sass rollup babel-cli babel-preset-
es2015-rollup  
  
ADD build.sh /root  
  
ENTRYPOINT ["nodemon", "--debug", "--legacy-watch", "--watch",
"/var/theme/scss", "--watch", "/var/theme/sass", "--watch", "/var/theme/es", "
--ext", "scss,js", "--exec", "/root/build.sh"]  

