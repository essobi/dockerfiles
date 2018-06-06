FROM debian:wheezy  
  
MAINTAINER Matt Kunkel matt@mrkunkel.com  
  
RUN groupadd -r homiehub && useradd -r -g homiehub homiehub  
  
RUN apt-get update && \  
apt-get install -y \  
python-minimal=2.7.3-4+deb7u1 \  
python-setuptools=0.6.24-1 \  
python-dev=2.7.3-4+deb7u1 && \  
easy_install pip && \  
pip install \  
pubnub==3.7.5 \  
influxdb==2.12.0 && \  
apt-get remove --auto-remove -y \  
python-setuptools \  
python-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /src  
ADD src/ /src  
  
USER homiehub  
  
CMD python homiehub.py  

