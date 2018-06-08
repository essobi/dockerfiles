FROM phusion/baseimage:latest  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Grab requirements.txt.  
ADD requirements.txt /tmp/requirements.txt  
  
RUN add-apt-repository ppa:deadsnakes/ppa; \  
apt-get update; \  
apt-get install -y \  
python3.6 \  
build-essential \  
python-dev \  
libatlas-dev \  
curl && \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3.6 get-pip.py && \  
rm get-pip.py && \  
ln -s /usr/bin/python3.6 /usr/local/bin/python3 && \  
pip3 install -qr /tmp/requirements.txt && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

