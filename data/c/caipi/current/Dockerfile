FROM node:6.9  
RUN apt-get update \  
&& apt-get install build-essential -y  
  
RUN wget http://download.redis.io/redis-stable.tar.gz \  
&& tar xvzf redis-stable.tar.gz \  
&& cd redis-stable \  
&& make \  
&& cp src/redis-server /usr/local/bin/ \  
&& cp src/redis-cli /usr/local/bin/  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \  
&& echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.2.list \  
&& apt-get update \  
&& apt-get install -y mongodb-org \  
&& mkdir /db/db -p  
  
RUN apt-get install -y python2.7 ruby-sass net-tools git  
  
RUN mkdir /home/www && echo "cd /home/www" > /root/.bashrc  
  
# RUN npm i -g npm@^3  
RUN curl -sL https://www.npmjs.org/install.sh | sh  
  
RUN npm i -g https://github.com/CaipiLabs/caipi  
  
EXPOSE 80:80  
RUN echo "ifconfig\ncaipi\nbash">/usr/local/bin/caipiDockerCli.sh \  
&& chmod a+x /usr/local/bin/caipiDockerCli.sh  
  
CMD redis-server --daemonize yes \  
&& mongod --fork --logpath /var/log/mongodb.log \  
&& cd /home/www \  
&& caipiDockerCli.sh  
  

