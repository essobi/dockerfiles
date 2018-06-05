FROM ubuntu:xenial  
  
######################################################################  
# DISCLAIMER #  
# #  
# THIS IS A PUBLIC DOCKER IMAGE, DON'T ADD FUNNEL INTERNALS TO HERE! #  
######################################################################  
# standard packages for Ubuntu 16.04 Xenial  
# and preload some expensive python modules  
# and disable nginx as not all use it  
# note: use as few RUN as possible as each creates a layer...  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
bzip2 \  
curl \  
openssl \  
python \  
python-dev \  
python-pip \  
libpq-dev \  
zip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
pip install --upgrade pip && \  
pip install psycopg2==2.6  

