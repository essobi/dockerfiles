FROM ferres/ds-dockers:base.cpu  
  
MAINTAINER Maxim Kochurov <maxim.v.kochurov@gmail.com>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-backports main
restricted universe multiverse" >> /etc/apt/sources.list && \  
apt-get -qq update && \  
apt-get install -y cmake \  
zlib1g-dev \  
libjpeg-dev \  
xvfb \  
libav-tools \  
xorg-dev \  
python-opengl \  
swig3.0 && \  
ln -s /usr/bin/swig3.0 /usr/bin/swig && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --upgrade pip \  
scipy \  
numpy && \  
pip3 install --upgrade sklearn \  
tqdm \  
gym[all] \  
seaborn && \  
pip3 install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip \  
https://github.com/yandexdataschool/AgentNet/archive/master.zip \  
keras

