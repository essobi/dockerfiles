FROM ubuntu:16.04  
MAINTAINER Bruce McCleave<bruce@thinkiq.com>  
  
USER root  
  
RUN apt-get update && \  
apt-get -y install software-properties-common && \  
apt-get update && \  
add-apt-repository ppa:fkrull/deadsnakes-python2.7 && \  
apt-get install -y sudo \  
curl \  
wget \  
tar \  
sudo \  
openssh-server \  
openssh-client \  
rsync \  
ntp && \  
apt-get install -y build-essential \  
libz-dev \  
libreadline-dev \  
libncursesw5-dev \  
libssl-dev \  
libgdbm-dev \  
libsqlite3-dev \  
libbz2-dev \  
liblzma-dev \  
tk-dev \  
libdb-dev \  
python2.7 && \  
apt-get install -y libatlas-base-dev \  
gfortran \  
python-pip && \  
groupadd -r thinkiq && sudo useradd thinkiq -s /bin/bash -g sudo -m && \  
echo "root ALL=(ALL) ALL" > /etc/sudoers && \  
echo "thinkiq ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
echo "Defaults env_reset" >>/etc/sudoers && \  
apt-get install -y python-numpy python-pip && \  
apt-get install -y python-scipy && \  
apt-get install -y python-matplotlib && \  
pip install --upgrade pip && \  
pip install scikit-learn && \  
pip install pandas && \  
pip install statsmodels && \  
pip install haversine && \  
pip install ipython && \  
pip install jupyter && \  
pip install kazoo && \  
pip install requests && \  
pip install mysql-connector==2.1.4 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
USER thinkiq  
WORKDIR /home/thinkiq  
ENV PATH=$PATH:/usr/local/python/bin/  
  
EXPOSE 9696 9797 9898  
VOLUME ["/home/thinkiq"]

