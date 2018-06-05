FROM ubuntu:bionic  
  
# Optimise environment variables  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 NOKOGIRI_USE_SYSTEM_LIBRARIES=true  
# Install system packages (ruby, python, node and build libraries)  
RUN apt-get update && \  
apt-get install --yes \  
build-essential ruby-dev ruby-bundler python3-dev python3-pip \  
libpq-dev libjpeg-dev zlib1g-dev libpng-dev libmagickwand-dev \  
libjpeg-progs optipng git vim curl jq python-launchpadlib libsodium-dev  
  
# Supportive python tools for debugging, syntax checking and DB connectivity  
RUN pip3 install --upgrade ipdb flake8 python-swiftclient psycopg2 pymongo
pipenv  
  
# Get nodejs  
RUN mkdir /usr/lib/nodejs && \  
curl https://nodejs.org/dist/v6.11.3/node-v6.11.3-linux-x64.tar.xz | tar -xJ
-C /usr/lib/nodejs && \  
mv /usr/lib/nodejs/node-v6.11.3-linux-x64 /usr/lib/nodejs/node-v6.11.3  
# Set nodejs paths  
ENV NODEJS_HOME=/usr/lib/nodejs/node-v6.11.3  
ENV PATH=$NODEJS_HOME/bin:$PATH  
  
# Latest Yarn package manager and bower  
RUN npm install --global yarn bower  
  
# Create a shared home directory - this helps anonymous users have a home  
ENV HOME=/home/shared LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN mkdir -p $HOME  
RUN mkdir -p $HOME/.cache/yarn/  
RUN mkdir -p $HOME/.cache/bower/  
RUN chmod -R 777 $HOME  
  

