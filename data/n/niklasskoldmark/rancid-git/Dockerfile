FROM ubuntu:14.04.2  
MAINTAINER Niklas Skoldmark <niklas.skoldmark@gmail.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install \  
-y \  
automake \  
debhelper \  
expect \  
git \  
liblockfile-simple-perl \  
libperl4-corelibs-perl \  
postfix \  
telnet \  
&& \  
apt-get clean && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone git://github.com/dotwaffle/rancid-git /srv/rancid-git && \  
cd /srv/rancid-git && \  
dpkg-buildpackage -uc -us && \  
cd /srv && \  
dpkg -i rancid*.deb && \  
rm -f -R /srv/rancid-git  
  
VOLUME /var/lib/rancid/data /var/lib/rancid/logs /var/lib/rancid/tmp
/root/secrets /root/configs  
  
COPY ["setup.sh", "/srv/setup.sh"]  
  
RUN /srv/setup.sh && rm /srv/setup.sh  
  
COPY ["entrypoint.sh", "/srv/entrypoint.sh"]  
  
ENTRYPOINT ["/srv/entrypoint.sh"]

