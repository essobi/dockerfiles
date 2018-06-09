FROM ubuntu:trusty  
  
MAINTAINER Patrick Liess <smrchy@gmail.com>  
  
VOLUME ["/srv/thumbor/storage"]  
  
RUN apt-get update && apt-get upgrade -y && apt-get -y install build-essential
checkinstall gcc python python-dev libpng12-dev libtiff5-dev libpng-dev
libjasper-dev libwebp-dev libcurl4-openssl-dev python-pgmagick libmagick++-dev
graphicsmagick libopencv-dev python-pip && apt-get clean  
  
RUN pip install pycurl numpy  
RUN pip install thumbor  
  
COPY thumbor.conf /etc/thumbor.conf  
ADD init /init  
RUN chmod +x /init  
CMD ["/init"]  

