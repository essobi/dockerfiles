FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
mercurial build-essential python-setuptools libxml2-dev python-dev \  
libxslt1-dev zlib1g-dev libffi-dev libssl-dev python-ipaddr \  
python-requests python-lxml python-pip python-yaml && \  
hg clone http://bitbucket.org/barnstorm/geni-lib && \  
cd geni-lib && \  
hg update -C 0.9-DEV && \  
pip install . && \  
cd / && \  
rm -r geni-lib && \  
apt-get remove -y --purge \  
mercurial build-essential python-setuptools libxml2-dev python-dev \  
libxslt1-dev zlib1g-dev libffi-dev libssl-dev && \  
apt-get autoremove -y --purge && \  
rm -fr /.cache/pip && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD cloudlab_util.py /usr/local/lib/python2.7/dist-packages/geni/  

