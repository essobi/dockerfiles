FROM ubuntu  
MAINTAINER Michal Belica <devel@beli.sk>  
EXPOSE 10000  
# runs as UID 1000 GID 1000 inside the container  
ENV VERSION 2.8.3  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
curl xpra python-qt4 python-pip python-setuptools \  
&& curl -o /tmp/Electrum-${VERSION}.tar.gz
https://download.electrum.org/${VERSION}/Electrum-${VERSION}.tar.gz \  
&& curl -o /tmp/Electrum-${VERSION}.tar.gz.asc
https://download.electrum.org/${VERSION}/Electrum-${VERSION}.tar.gz.asc \  
&& gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys
0x2bd5824b7f9470e6 \  
&& gpg --list-keys '0x6694D8DE7BE8EE5631BED9502BD5824B7F9470E6' \  
&& gpg --verify /tmp/Electrum-${VERSION}.tar.gz.asc
/tmp/Electrum-${VERSION}.tar.gz \  
&& pip install /tmp/Electrum-${VERSION}.tar.gz \  
&& test -f /usr/local/bin/electrum \  
&& rm -vrf /tmp/Electrum-${VERSION}.tar.gz /tmp/Electrum-${VERSION}.tar.gz.asc
${HOME}/.gnupg \  
&& apt-get purge --autoremove -y python-pip python-setuptools curl \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# disable starting of other programs in default xpra.conf  
RUN sed -ie 's/^start-child/#start-child/' /etc/xpra/xpra.conf  
  
RUN useradd -d /home/user -m user \  
&& mkdir /electrum \  
&& ln -s /electrum /home/user/.electrum \  
&& chown user:user /electrum  
USER user  
ENV HOME /home/user  
WORKDIR /home/user  
VOLUME /electrum  
  
CMD ["/usr/bin/xpra", "start", ":100", "--start-
child=/usr/local/bin/electrum", "--bind-tcp=0.0.0.0:10000", "--no-daemon", "--
no-notifications", "--no-mdns", "--no-pulseaudio", "--exit-with-children"]  

