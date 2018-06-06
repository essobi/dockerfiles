FROM wasnot/chainer-appengine:0.1.1  
MAINTAINER Wasnot <wasnot@example.com>  
RUN \  
apt-get update && apt-get upgrade -y && \  
apt-get install libopencv-dev python-opencv -y && \  
ln /dev/null /dev/raw1394  
  
ENV PYTHONPATH $PYTHONPATH:/usr/lib/python2.7/dist-packages/  

