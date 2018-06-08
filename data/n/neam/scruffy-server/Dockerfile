FROM ubuntu:trusty  
MAINTAINER Fredrik Wollsén <fredrik@neam.se>  
RUN \  
apt-get update &&\  
apt-get install -y python-pip python-dev python-setuptools graphviz plotutils
\  
librsvg2-bin git python-pil fonts-tlwg-purisa libjpeg-dev zlib1g-dev  
  
WORKDIR /opt  
  
RUN \  
git clone https://github.com/aivarsk/scruffy.git &&\  
cd scruffy &&\  
python setup.py install &&\  
cd \- &&\  
rm -rf scruffy  
  
RUN \  
git clone https://github.com/wernight/scruffy-server.git &&\  
cd scruffy-server &&\  
pip install -r requirements.txt  
  
RUN \  
apt-get remove -y --purge python-pip python-dev python-setuptools git &&\  
apt-get clean &&\  
apt-get autoremove -y &&\  
rm -rf /var/cache/apt/*  
  
WORKDIR /opt/scruffy-server  
CMD python server.py  
EXPOSE 8080  

