FROM ubuntu:14.04  
MAINTAINER Tomasz Cholewa <slashroot@slashroot.eu>  
  
RUN apt-get update && apt-get install -y ruby-dev gcc make rpm dpkg-sig  
RUN gem install fpm  
  
VOLUME /src  
VOLUME /dst  
  
CMD /usr/local/bin/fpm  
  

