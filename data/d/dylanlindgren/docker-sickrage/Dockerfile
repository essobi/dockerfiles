FROM debian:wheezy  
  
MAINTAINER “Dylan Lindgren” <dylan.lindgren@gmail.com>  
  
WORKDIR /var/lib  
  
RUN echo 'deb ftp://ftp.us.debian.org/debian/ wheezy non-free' >>
/etc/apt/sources.list.d/wheezy.non-free.list  
RUN echo 'deb http://security.debian.org/ wheezy/updates non-free' >>
/etc/apt/sources.list.d/wheezy.non-free.list  
  
# Install SickRage & it's prerequisites  
RUN apt-get update -y && \  
apt-get install -y \  
git \  
wget \  
python-dev \  
libffi-dev \  
unrar \  
python3-openssl \  
libssl-dev && \  
rm -rf /var/lib/apt/lists/* && \  
git clone https://github.com/SickRage/SickRage.git /var/lib/SickRage  
# Create SickBeard user and set permissions  
RUN adduser -c "SickRage User" sickrage && \  
mkdir -p /data/sickrage && \  
chown -R sickrage:sickrage /var/lib/SickRage /data/sickrage  
VOLUME ["/data/sickrage"]  
VOLUME ["/data/tvshows"]  
VOLUME ["/data/transmission"]  
  
EXPOSE 8081  
  
USER sickrage  
  
ENTRYPOINT ["/usr/bin/python", "/var/lib/SickRage/SickBeard.py", "--nolaunch",
"--datadir=/data/sickrage"]  

