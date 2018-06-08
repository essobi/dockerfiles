FROM debian  
MAINTAINER Kevin Larsonneur <klarsonneur@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
RUN apt-get -y install owfs usbutils supervisor  
  
ADD supervisor.owserver.conf /etc/supervisor/conf.d/owserver.conf  
RUN mkdir /owfs  
  
VOLUME ["/owfs"]  
CMD ["supervisord", "-n"]  

