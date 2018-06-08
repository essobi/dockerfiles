FROM ubuntu  
MAINTAINER Gebhard Woestemeyer <g.woestemeyer@gmail.com>  
RUN \  
apt-get update &&\  
apt-get install -y python-dev python-setuptools graphviz plotutils \  
librsvg2-bin git python-pil fonts-tlwg-purisa  
  
RUN \  
git clone https://github.com/aivarsk/scruffy.git &&\  
cd scruffy &&\  
python setup.py install &&\  
cd \- &&\  
rm -rf scruffy  
  
RUN \  
apt-get remove -y \--purge python-dev python-setuptools git &&\  
apt-get clean &&\  
apt-get autoremove -y &&\  
rm -rf /var/cache/apt/*  
  
ENTRYPOINT ["/usr/local/bin/suml"]  

