# gotchas/pharo-base64  
FROM ubuntu:14.04  
MAINTAINER CAs  
  
#RUN dpkg --add-architecture i386  
RUN apt-get update -q  
RUN apt-get -qy --no-install-recommends install \  
libfreetype6 \  
curl \  
unzip  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#CMD ["/opt/pharo","Pharo.image","--no-quit"]  
CMD ["./pharo","Pharo.image","--no-quit"]  
  
RUN echo "Dependencies for Pharo are installed"  

