FROM ubuntu:trusty  
MAINTAINER Gustavo Lopes <gustavo@thehyve.nl>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 3375DA21 && \  
echo deb http://apt.thehyve.net/internal/ trusty main >
/etc/apt/sources.list.d/internal.list && \  
apt-get update -q && \  
apt-get install -y --no-install-recommends \  
ruby-dev bsdtar sudo \  
make gcc g++ pkg-config binutils \  
git curl wget \  
facter lsb-release && \  
rm -rf /var/lib/apt/lists/* && \  
gem install --no-ri --no-rdoc -v 1.6.1 fpm && \  
echo 'user ALL=(ALL:ALL) NOPASSWD: ALL' >> /etc/sudoers && \  
curl -L -f -o /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.9/gosu-$(dpkg --print-
architecture)" && \  
chmod +x /usr/local/bin/gosu  
  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.0/dumb-
init_1.1.0_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
ADD entrypoint /  
ENTRYPOINT [ "dumb-init", "/entrypoint" ]  

