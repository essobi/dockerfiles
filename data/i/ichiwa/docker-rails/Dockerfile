FROM ruby:2.2  
MAINTAINER ichiwa  
  
ARG NODE_VERSION="6.10.3"  
ENV LANG C.UTF-8  
RUN apt-get update -qq && apt-get install -y \  
build-essential \  
libpq-dev \  
apt-utils \  
libmysqld-dev \  
libmysqlclient-dev \  
mysql-client \  
node \  
npm  
RUN npm cache clean && npm install n bower -g  
RUN n $NODE_VERSION && n use $NODE_VERSION && ln -sf /usr/local/bin/node
/usr/bin/node  
RUN apt-get purge -y nodejs npm  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
  

