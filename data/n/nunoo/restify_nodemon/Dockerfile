FROM ubuntu:latest  
MAINTAINER Matt Koski <maccam912@gmail.com>  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list  
  
RUN apt-get update -y  
#RUN apt-get install -y mongodb-org  
RUN apt-get install -y git python build-essential curl ca-certificates  
#RUN service mongodb start  
#RUN mkdir -p /data/db  
RUN mkdir /Development  
# Install node from repo  
#RUN cd /Development && git clone git://github.com/joyent/node  
#RUN cd /Development/node && ./configure && make && make install  
RUN mkdir /nodejs && curl
http://nodejs.org/dist/v0.10.28/node-v0.10.28-linux-x64.tar.gz | tar xvzf - -C
/nodejs --strip-components=1  
  
ENV PATH $PATH:/nodejs/bin  
  
# Make sure npm is at it's latest  
RUN npm install npm@latest -g  
  
# Finish installing node  
# Install restify, nodemon  
RUN npm install -g restify nodemon coffee-script  
# RUN npm install -g yo bower grunt-cli generator-meanjs express  
# RUN curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh  
EXPOSE 80:80  
EXPOSE 443:443  
EXPOSE 3000:3000  
RUN echo "\n##############################\n1. Create a new user with adduser,
'su' into that user.\n2. 'yo meanjs' to scaffold your app in the current
directory.\n3. Start mongo in the background (e.g. 'mongod
&')\n##############################\n"  

