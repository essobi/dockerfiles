FROM node:6.9.4  
MAINTAINER Vinicius <vinicius.ribeiro.carneiro@gmail.com>  
LABEL node="6.9.4" mongodb="3.4" redis="3.2.6" yarn="0.18.1"  
ENV DEBIAN_FRONTEND=noninteractive  
  
# some node packages  
RUN npm install -g yarn@0.18.1 nodemon  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6 \  
&& echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.4 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.4.list \  
&& apt-get update \  
&& apt-get install -y mongodb-org --no-install-recommends \  
&& apt-get install -y build-essential tcl8.5 libsqlite3-dev ruby ruby-dev
build-essential \  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# redis  
RUN wget http://download.redis.io/releases/redis-3.2.6.tar.gz \  
&& tar xzf redis-3.2.6.tar.gz \  
&& rm redis-3.2.6.tar.gz \  
&& cd redis-3.2.6 \  
&& make \  
&& make install \  
&& cd utils \  
&& ./install_server.sh  
  
# mailcatcher  
RUN gem install --no-ri --no-rdoc mailcatcher  
RUN mkdir -p /scripts  
COPY scripts/ /scripts/  
EXPOSE 27017 6379 1080 1025

