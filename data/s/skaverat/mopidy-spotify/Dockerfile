FROM phusion/baseimage  
MAINTAINER SkaveRat <skaverat@funlynx.de>  
  
RUN curl --silent http://apt.mopidy.com/mopidy.gpg | sudo apt-key add -  
RUN curl --silent http://apt.mopidy.com/mopidy.list >
/etc/apt/sources.list.d/mopidy.list  
RUN apt-get update  
RUN apt-get install -y mopidy mopidy-spotify  
  
ADD mopidy.conf /root/.config/mopidy/mopidy.conf  
  
CMD ["/usr/bin/mopidy"]  

