FROM debian:jessie  
MAINTAINER zach@mavenclinic.com  
  
VOLUME ["/srv/thumbor/storage"]  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
python-pycurl python-pip python-dev python-numpy python-opencv wget webp
libpng-dev libtiff-dev libjasper-dev libjpeg-dev \  
&& apt-get clean  
  
# this is a hack but needed for some reason  
RUN pip install colour && cd /usr/local/lib/python2.7/dist-packages && wget
https://raw.githubusercontent.com/vaab/colour/master/colour.py  
RUN pip install thumbor==4.4.1 opencv-engine  
  
COPY thumbor.conf /etc/thumbor.conf  
COPY init /init  
  
EXPOSE 80  
CMD ["/init"]  

