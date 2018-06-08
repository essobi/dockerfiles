FROM ubuntu:16.04  
MAINTAINER Sangjee Dondrub <sangjeedondrub@live.com>  
LABEL version="1.0"  
LABEL description="A ubuntu docker image, with Chinese sourcelist and aliyun
pip source"  
  
ENV HOME /root  
  
COPY sources.list /etc/apt/sources.list  
  
RUN apt-get update -y && \  
apt-get install -y zsh \  
python \  
python-pip \  
python-setuptools \  
python-dev \  
vim \  
git \  
curl \  
build-essential \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /root/.pip \  
&& pip install --upgrade pip \  
&& chsh -s /usr/bin/zsh \  
&& apt-get clean \  
&& apt-get autoremove  
  
COPY bashrc /root/.bashrc  
COPY vimrc /root/.vimrc  
COPY solarized.vim /root/.vim/colors/solarized.vim  
COPY pip.conf /root/.pip/pip.conf  
  
WORKDIR /root  
  
CMD ["/bin/bash"]  

