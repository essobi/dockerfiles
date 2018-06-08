FROM monokrome/node  
MAINTAINER Brandon R. Stoner <brandon@rentlytics.com>  
  
WORKDIR /usr/local/share/renderize  
ADD ./ /usr/local/share/renderize  
  
RUN apt-get install -y wget bzip2 libfreetype6 libfontconfig1 python-software-
properties python g++ make && wget
http://phantomjs.googlecode.com/files/phantomjs-1.9.2-linux-x86_64.tar.bz2 &&
tar -xjf phantomjs-1.9.2-linux-x86_64.tar.bz2 && cp
phantomjs-1.9.2-linux-x86_64/bin/phantomjs /usr/local/bin/ && rm -rf
phantomjs-1.9.2-linux-x86_64  
RUN npm install --production  
RUN apt-get purge -y python-software-properties python g++ make bzip2 wget  
  
EXPOSE 9040  
CMD ./node_modules/.bin/coffee server.coffee  

