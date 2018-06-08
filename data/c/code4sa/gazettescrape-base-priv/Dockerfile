FROM ubuntu:trusty  
  
COPY requirements.txt /tmp/requirements.txt  
  
# easyinstalling pip and then upgrading pip and setuptools is a workaround  
# noted in https://bugs.launchpad.net/ubuntu/+source/python-
pip/+bug/1658844/comments/14  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -y && \  
apt-get install -y python-pip \  
python-dev \  
libncurses5-dev \  
libpq-dev \  
python-psycopg2 \  
libxml2-dev \  
libxslt-dev \  
libffi-dev \  
qpdf \  
poppler-utils &&\  
easy_install pip &&\  
pip install -U pip setuptools &&\  
pip install -r /tmp/requirements.txt && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
ln -snf /bin/bash /bin/sh \  

