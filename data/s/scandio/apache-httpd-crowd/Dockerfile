FROM ubuntu:14.04  
MAINTAINER Scandio GmbH  
  
# Environment variables for Atlassian Crowd  
ENV CROWD_CONNECTOR_DOWNLOAD_URL https://github.com/fgimian/cwdapache.git  
ENV CROWD_CONNECTOR_VERSION 2.3  
ENV IMPORTCERT false  
ENV IMPORTCERTPATH /root/docker/certs  
  
# Install Apache2  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y --no-install-recommends \  
apache2 \  
apache2-mpm-worker \  
gettext-base \  
libcurl4-openssl-dev \  
lynx \  
curl \  
ca-certificates \  
&& apt-get autoremove -y \  
&& rm -r /var/lib/apt/lists/*  
  
# Build Atlassian Crowd Apache Connector  
RUN buildDeps=' \  
autoconf \  
automake \  
apache2-threaded-dev \  
git \  
libtool \  
libsvn-dev \  
libxml2-dev \  
libapache2-svn \  
make \  
' \  
  
# Install build dependencies  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
  
# Download Atlassian Crowd Connector  
&& mkdir -p /usr/local/src/crowd \  
&& cd /usr/local/src/crowd \  
&& git clone ${CROWD_CONNECTOR_DOWNLOAD_URL} . \  
&& git checkout tags/${CROWD_CONNECTOR_VERSION} \  
  
# Build and install Atlassian Crowd Connector  
&& aclocal \  
&& libtoolize \  
&& autoheader \  
&& automake --force-missing --add-missing \  
&& autoreconf \  
&& ./configure \  
&& make \  
&& make install \  
&& libtool --finish /usr/local/lib \  
  
# Remove build files/folders and build dependencies  
&& rm -r /usr/local/src/crowd \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -r /var/lib/apt/lists/*  
  
RUN mkdir -p /root/docker/apache2  
COPY conf/security.conf /root/docker/apache2/conf/  
COPY conf/ssl.conf /root/docker/apache2/conf/  
COPY init/configure-and-start.sh /root/docker/apache2/  
COPY init/reverse-proxy.conf.template /root/docker/apache2/  
  
EXPOSE 80 443  
VOLUME ["/var/log/apache2", "/etc/apache2"]  
  
CMD ["/root/docker/apache2/configure-and-start.sh"]  

