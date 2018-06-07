FROM node:4.8.0  
MAINTAINER Alex T<alex@tzapu.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq && apt-get install -y locales -qq && locale-gen
en_US.UTF-8 en_us && dpkg-reconfigure locales && locale-gen C.UTF-8 &&
/usr/sbin/update-locale LANG=C.UTF-8  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
#RUN ln -s /usr/local/bin/node /usr/local/bin/nodejs  
RUN curl -sL https://install.meteor.com/?release=1.4.4.1 | sed s/--progress-
bar/-sL/g | /bin/sh  
  
RUN set -x \  
&& git clone -b alienbus https://github.com/etamity/Rocket.Chat.git /opt/app  
  
WORKDIR /opt/app/  
ADD . /opt/app/  
RUN meteor npm install  
  
VOLUME /opt/app/  
  
# needs a mongoinstance - defaults to container linking with alias 'mongo'  
ENV DEPLOY_METHOD=docker \  
NODE_ENV=production \  
MONGO_URL=mongodb://mongo:27017/alienbus \  
MONGO_OPLOG_URL=mongodb://mongo:27017/local \  
HOME=/tmp \  
PORT=3000 \  
ROOT_URL=http://localhost:3000 \  
Accounts_AvatarStorePath=/app/uploads  
  
EXPOSE 3000  
CMD meteor;

