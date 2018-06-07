# Pull in base image  
FROM vrtsystems/baseimage:0.2.0  
MAINTAINER VRT Engineering <engineering@vrt.com.au>  
  
# Update repostory cache and install dependencies for sniproxy  
# For reasons unknown, a deb package is not provided by Debian.  
RUN apt-get update \  
&& apt-get -y install cdbs debhelper dh-autoreconf autotools-dev \  
gettext pkg-config libev-dev libpcre3-dev libudns-dev \  
build-essential wget dpkg-dev \  
&& echo "=== Retrieving package =================" \  
&& wget -O /tmp/sniproxy_0.4.0.tar.gz \  
https://github.com/dlundquist/sniproxy/archive/0.4.0.tar.gz \  
&& echo "=== Building package ===================" \  
&& ( cd /tmp && tar -xzvf sniproxy_0.4.0.tar.gz \  
&& cd /tmp/sniproxy-0.4.0 \  
&& ./autogen.sh \  
&& dpkg-buildpackage -us -uc -b ) \  
&& echo "=== Installing package =================" \  
&& dpkg -i /tmp/*.deb \  
&& echo "=== Cleaning up ========================" \  
&& rm -fr /tmp/sniproxy* \  
&& apt-get purge -y debhelper dh-autoreconf autotools-dev wget dpkg-dev \  
pkg-config libev-dev libpcre3-dev libudns-dev build-essential \  
&& /usr/local/sbin/docker-cleanup.sh  
  
# Expose ports for sniproxy  
EXPOSE 443/tcp  
EXPOSE 80/tcp  
  
# Copy configuration generator script  
COPY runsniproxy.sh /usr/local/sbin/runsniproxy.sh  
  
# Copy supervisord configuration for sniproxy  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Command to run when starting the container  
CMD ["supervisord"]  

