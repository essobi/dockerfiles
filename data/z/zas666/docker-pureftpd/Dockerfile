# ftp server  
#  
# VERSION 0.0.2  
#  
# Links:  
# - https://help.ubuntu.com/community/PureFTP  
# - http://www.dikant.de/2009/01/22/setting-up-pureftpd-on-a-virtual-server/  
# - http://download.pureftpd.org/pub/pure-ftpd/doc/README  
FROM ubuntu:14.04  
MAINTAINER Laurent Monin <zas+docker@metabraiz.org>  
  
COPY ./files/nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get -y --force-yes --no-install-recommends install \  
debhelper \  
dpkg-dev \  
openbsd-inetd \  
python \  
python-setuptools \  
rsyslog \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install supervisord (used to handle processes)  
# ----------------------------------------------  
#  
# Installation with easy_install is more reliable. apt-get don't always work.  
RUN easy_install supervisor  
  
#  
# Download and build pure-ftp  
# ---------------------------  
RUN apt-get update \  
&& apt-get -y build-dep pure-ftpd \  
&& mkdir /tmp/pure-ftpd/ \  
&& cd /tmp/pure-ftpd/ \  
&& apt-get source pure-ftpd \  
&& cd pure-ftpd-* \  
&& sed -i '/^optflags=/ s/$/ --without-capabilities/g' ./debian/rules \  
&& dpkg-buildpackage -b -uc \  
&& dpkg -i /tmp/pure-ftpd/pure-ftpd-common*.deb /tmp/pure-ftpd/pure-ftpd_*.deb
\  
&& apt-mark hold pure-ftpd pure-ftpd-common \  
&& rm -rf /var/lib/apt/lists/*  
  
#RUN apt-get update && apt-get build-dep -y pure-ftpd && rm -rf
/var/lib/apt/lists/*  
#  
#RUN mkdir -p /build \  
#&& wget --no-check-certificate -O - http://download.pureftpd.org/pub/pure-
ftpd/releases/pure-ftpd-1.0.42.tar.gz | tar xzC /build --strip-components=1 \  
#&& cd /build \  
#&& ./configure --with-everything --with-privsep --with-paranoidmsg --with-
virtualchroot --without-pam --without-capabilities \  
#&& make \  
#&& make install \  
#&& rm -rf /build  
#  
# Setup users, add as many as needed  
# ----------------------------------  
RUN groupadd ftpgroup  
RUN useradd -g ftpgroup -m -d /home/ftpusers -s /usr/sbin/nologin ftpuser  
RUN useradd -g ftpgroup -m -d /home/ftp -s /usr/sbin/nologin ftp  
  
# Configure supervisord (used to handle processes)  
# ----------------------------------------------  
#  
COPY ./files/etc-supervisord.conf /etc/supervisord.conf  
COPY ./files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN mkdir -p /var/log/supervisor/  
  
#  
# Setup rsyslog  
# ---------------------------  
COPY ./files/etc-rsyslog.conf /etc/rsyslog.conf  
COPY ./files/etc-rsyslog.d-50-default.conf /etc/rsyslog.d/50-default.conf  
  
#  
# Configure pure-ftpd  
# -------------------  
RUN mkdir -p /etc/pure-ftpd/conf  
COPY ./files/conf/* /etc/pure-ftpd/conf/  
  
#  
# Start things  
# -------------  
COPY ./files/start.sh /start.sh  
CMD ["/start.sh"]  
  
EXPOSE 20 21 30000 30001 30002 30003 30004 30005 30006 30007 30008 30009  
#  
# Set up volumes  
# --------------  
VOLUME /home/ftpusers  
VOLUME /home/ftp  

