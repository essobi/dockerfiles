FROM ozzyjohnson/cuda  
  
MAINTAINER Ozzy Johnson <docker@ozzy.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV FAH_RELEASE 7.4  
ENV FAH_VERSION 7.4.4  
ENV FAH_INSTALL https://fah.stanford.edu/file-
releases/public/release/fahclient/debian-
testing-64bit/v${FAH_RELEASE}/fahclient_${FAH_VERSION}_amd64.deb  
  
# The Folding client GPU tasks depend on libc > 2.15, stable is 2.13.  
RUN echo "deb http://ftp.debian.org/debian testing main" >>
/etc/apt/sources.list  
  
# Update and install minimal.  
RUN \  
apt-get \  
update \  
\--quiet \  
&& apt-get \  
install \  
-f \  
\--yes \  
\--no-install-recommends \  
\--no-install-suggests \  
adduser=3.113+nmu3 \  
libc6=2.19-12 \  
&& wget \  
$FAH_INSTALL \  
-P /tmp \  
\--no-verbose \  
\--no-check-certificate \  
&& dpkg \  
-i \  
\--force-depends \  
/tmp/fahclient_${FAH_VERSION}_amd64.deb \  
&& rm /tmp/* \  
  
  
# Clean up packages.  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Data volume.  
ONBUILD VOLUME /data  
  
# Getting ready.  
WORKDIR /data  
  
# Default command.  
ENTRYPOINT ["/usr/bin/FAHClient"]  

