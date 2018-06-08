FROM phusion/baseimage:0.9.18  
MAINTAINER needo <needo@superhero.org>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe
multiverse" && \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates
universe multiverse" && \  
apt-get update -q && \  
  
# Install Dependencies  
apt-get install -qy ca-certificates wget unrar unzip git build-essential
libssl-dev libffi-dev autoconf \  
automake bzip2 file g++ gcc imagemagick libbz2-dev libc6-dev libcurl4-openssl-
dev libevent-dev \  
libgeoip-dev libglib2.0-dev libjpeg-dev liblzma-dev libmagickcore-dev
libmagickwand-dev \  
libmysqlclient-dev libncurses-dev libpng-dev libpq-dev libreadline-dev
libsqlite3-dev \  
libtool libwebp-dev libxml2-dev libxslt-dev libyaml-dev make patch xz-utils
zlib1g-dev && \  
  
# clean up  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
/usr/share/man /usr/share/groff /usr/share/info \  
/usr/share/lintian /usr/share/linda /var/cache/man && \  
(( find /usr/share/doc -depth -type f ! -name copyright -print0|xargs -0 rm ||
true )) && \  
(( find /usr/share/doc -empty|xargs rmdir || true ))  
  
# Install SickRage 2016.04.01-1  
RUN mkdir /opt/sickrage && \  
cd /tmp && \  
wget https://github.com/SickRage/SickRage/archive/2016.04.01-1.zip -O
sickrage.zip && \  
unzip sickrage.zip && \  
rm sickrage.zip && \  
mv SickRage-*/* /opt/sickrage/ && \  
chown -R nobody:users /opt/sickrage  
  
ENV PYTHON_VERSION 2.7.10  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 7.1.2  
COPY install_python.sh /  
RUN chmod +x /install_python.sh && \  
/bin/bash /install_python.sh && \  
rm -f /install_python.sh  
  
EXPOSE 8081  
# SickRage Configuration  
VOLUME /config  
  
# Downloads directory  
VOLUME /downloads  
  
# TV directory  
VOLUME /tv  
  
# Add edge.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD edge.sh /etc/my_init.d/edge.sh  
RUN chmod +x /etc/my_init.d/edge.sh  
  
# Add SickRage to runit  
RUN mkdir /etc/service/sickrage  
ADD sickrage.sh /etc/service/sickrage/run  
RUN chmod +x /etc/service/sickrage/run  

