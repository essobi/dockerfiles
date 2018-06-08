# nodeapp  
# This is a pretty generic node app dockerfile  
FROM node:0.10  
MAINTAINER Joey Baker <joey@getable.com>  
  
# set ENV  
ENV NODE_ENV production  
  
# ensure we have the latest npm and node  
RUN npm i -g npm \  
&& npm i -g nave \  
&& nave usemain 0.10.38 \  
# constructble uses git, make sure we're up-to-date there  
&& apt-get update -qq \  
&& apt-get install -y git  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pgp.mit.edu --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# Bundle app source  
ONBUILD ADD . /src  
  
# add a user and set permissions  
ONBUILD RUN groupadd -r nodeapp \  
&& useradd -d /var/lib/nodeapp -g nodeapp nodeapp \  
&& chown -R nodeapp:nodeapp /src \  
&& chmod -R g+rw /src  
  
EXPOSE 80  
WORKDIR /src  
CMD ["gosu", "nodeapp", "npm", "start"]  

