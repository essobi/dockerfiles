FROM ubuntu  
MAINTAINER George Rappel <george.concei@hotmail.com>  
  
WORKDIR /src  
  
RUN apt-get install -y software-properties-common python  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise universe" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y nodejs  
  
ADD [^.]* /src/  
ADD ./commands /src/commands  
  
RUN npm install /src/  
  
CMD ["/usr/bin/node", "/src/app.js"]

