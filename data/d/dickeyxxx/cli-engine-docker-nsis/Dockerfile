FROM ubuntu:16.04  
  
MAINTAINER Jeff Dickey  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen  
  
RUN apt-get -y update && apt-get install -y \--no-install-recommends \  
curl \  
git \  
ca-certificates \  
ssh \  
osslsigncode \  
python-dev \  
locales \  
apt-transport-https \  
nsis \  
p7zip-full \  
xz-utils \  
&& \  
curl https://bootstrap.pypa.io/get-pip.py | python && \  
pip install awscli --upgrade && \  
aws configure set preview.cloudfront true && \  
locale-gen && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
curl -sL https://deb.nodesource.com/setup_9.x | bash - && \  
apt-get install -y \--no-install-recommends nodejs yarn && \  
apt-get clean && apt-get -y autoremove && \  
rm -rf \  
/var/lib/apt/lists/* \  
/root/.cache/* \  
/var/cache/*  
  
CMD bash  

