FROM debian:jessie  
MAINTAINER Ivan Porto Carrero <ivan@flanders.co.nz> (@casualjim)  
  
RUN set -eux &&\  
apt-get update -yqq &&\  
apt-get upgrade -yqq &&\  
apt-get install -yqq --no-install-recommends build-essential ruby-dev rubygems
rpm libffi-dev bsdtar &&\  
gem install --quiet --no-rdoc --no-ri fpm &&\  
gem sources -c &&\  
apt-get clean -y &&\  
apt-get autoclean -yqq &&\  
apt-get autoremove -yqq &&\  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /usr/share/doc/*
/usr/share/locale/* /var/cache/debconf/*-old  
  
ENTRYPOINT ["fpm"]  
CMD ["--help"]  

