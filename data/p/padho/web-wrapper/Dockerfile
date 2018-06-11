FROM ubuntu:xenial  
  
RUN sed -i -e "s|http://archive.ubuntu.com/|http://jp.archive.ubuntu.com/|"
/etc/apt/sources.list  
  
RUN apt update \  
&& apt install -y curl git libfontconfig-dev fonts-takao* supervisor sudo \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt install -y nodejs  
  
RUN cd /usr/local/src \  
&& curl -OL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
&& tar -xf phantomjs-2.1.1-linux-x86_64.tar.bz2 \  
&& cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/  
  
# Install app dependencies  
COPY package.json /www/package.json  
RUN cd /www; npm install && npm install -g nodemon  
  
# Copy app source  
COPY . /www  
  
# Set work directory to /www  
WORKDIR /www  
  
# set your port  
ENV PORT 8080  
# expose the port to outside world  
EXPOSE 8777  
# start command as per package.json  
CMD ["npm", "run", "dev"]  

