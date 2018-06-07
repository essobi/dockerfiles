FROM ubuntu:14.04  
MAINTAINER Ensky Lin <enskylin@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
# setup our Ubuntu sources (ADD breaks caching)  
RUN echo "deb http://tw.archive.ubuntu.com/ubuntu/ trusty main\n\  
deb http://tw.archive.ubuntu.com/ubuntu/ trusty multiverse\n\  
deb http://tw.archive.ubuntu.com/ubuntu/ trusty universe\n\  
deb http://tw.archive.ubuntu.com/ubuntu/ trusty restricted\n\  
deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu trusty main\n\  
" >> /etc/apt/sources.list  
  
# no Upstart or DBus  
# https://github.com/dotcloud/docker/issues/1724#issuecomment-26294856  
RUN apt-mark hold initscripts udev plymouth mountall \  
&& dpkg-divert --local --rename \--add /sbin/initctl \  
&& ln -sf /bin/true /sbin/initctl  
  
RUN apt-key adv --recv-keys \--keyserver keyserver.ubuntu.com B9316A7BC7917B12
\  
&& apt-get update \  
&& apt-get install -y \--force-yes software-properties-common python-software-
properties \  
&& apt-add-repository ppa:freenx-team/trusty \  
&& apt-get update \  
&& apt-get install -y \--force-yes --no-install-recommends supervisor wget \  
openssh-server pwgen sudo vim-tiny \  
net-tools \  
gtk2-engines-murrine ttf-ubuntu-font-family \  
ibus ibus-clutter ibus-gtk ibus-gtk3 ibus-qt4 ibus-chewing \  
&& apt-get install -y \--force-yes xfce4 xfce4-goodies freenx-server \  
libreoffice libreoffice-gnome firefox \  
ttf-wqy-zenhei language-pack-zh-hant language-pack-zh-hant-base
libreoffice-l10n-zh-tw \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://bugs.launchpad.net/freenx-
server/+bug/576359/+attachment/1378450/+files/nxsetup.tar.gz \  
&& tar -xvf nxsetup.tar.gz \  
&& mv nxsetup /usr/lib/nx/nxsetup \  
&& rm nxsetup*  
  
ADD startup.sh /  
ADD supervisord.conf /  
  
EXPOSE 22  
WORKDIR /  
ENTRYPOINT ["/startup.sh"]  

