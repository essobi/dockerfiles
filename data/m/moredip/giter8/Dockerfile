FROM frolvlad/alpine-oraclejdk8:slim  
MAINTAINER docker@thepete.net  
LABEL Description="A simple containerization of giter8.
https://github.com/moredip/giter8"  
  
RUN apk --update add curl  
  
# install conscript  
RUN curl https://raw.githubusercontent.com/n8han/conscript/master/setup.sh |
sh  
  
# install giter8 using conscript  
RUN ~/bin/cs n8han/giter8  
  
# trigger g8 to install dependencies, including half the internet apparently  
RUN ~/bin/g8; true  
  
VOLUME /g8out  
WORKDIR /g8out  
  
ENTRYPOINT ["/home/conscript/bin/g8","--force"]  

