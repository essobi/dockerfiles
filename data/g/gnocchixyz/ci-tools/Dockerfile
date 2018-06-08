FROM ubuntu:16.04  
ENV GNOCCHI_SRC /home/tester/src  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && apt-get install -qy \  
locales \  
git \  
wget \  
nodejs \  
nodejs-legacy \  
npm \  
python \  
python3 \  
python-dev \  
python3-dev \  
# Needed for uwsgi core routing support  
libpcre3-dev \  
python-pip \  
build-essential \  
libffi-dev \  
libpq-dev \  
postgresql \  
memcached \  
mysql-client \  
mysql-server \  
# For Ceph  
librados-dev \  
liberasurecode-dev \  
python-rados \  
ceph \  
# For prometheus  
libsnappy-dev \  
libprotobuf-dev  
  
# Install Redis from more recent version of Ubuntu to have >= 3.2 and not only
3.0  
RUN echo 'deb http://archive.ubuntu.com/ubuntu artful universe' >
/etc/apt/sources.list  
RUN apt-get update -y && apt-get install -qy \  
redis-server \  
&& rm -rf /var/lib/apt/lists/*  
  
#NOTE(sileht): really no utf-8 in 2017 !?  
ENV LANG en_US.UTF-8  
RUN update-locale  
RUN locale-gen $LANG  
  
#NOTE(sileht): Upgrade python dev tools  
RUN pip install -U pip tox virtualenv  
  
RUN npm install s3rver@1.0.3 --global  
  
RUN groupadd --gid 2000 tester  
RUN useradd --uid 2000 --gid 2000 --create-home --shell /bin/bash tester  
USER tester  
  
WORKDIR $GNOCCHI_SRC  

