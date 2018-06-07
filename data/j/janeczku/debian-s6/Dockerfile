FROM debian:jessie-backports  
MAINTAINER Jan Broer <janeczku@yahoo.com>  
  
##  
## ROOTFS  
##  
COPY rootfs /  
  
##  
## PREPARE  
##  
# Configure apt  
RUN \  
# Prepare system  
apt-wrap apt-get update \  
&& apt-wrap apt-get install -y --no-install-recommends apt-utils \  
  
# Fix locales  
&& apt-wrap apt-get install -y --no-install-recommends locales \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
  
# Upgrade all packages  
&& apt-wrap apt-get dist-upgrade -y --no-install-recommends \  
  
# Clean up  
&& apt-clean  
  
ENV LANG en_US.utf8  
  
##  
## S6 OVERLAY  
##  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.16.0.2/s6-overlay-amd64.tar.gz
/tmp/s6-overlay-amd64.tar.gz  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.16.0.2/s6-overlay-amd64.tar.gz.sig
/tmp/s6-overlay-amd64.tar.gz.sig  
RUN \  
# Verify GPG signature - "Just Containers <just-containers@jrjrtech.com>"  
gpg --keyserver pgp.mit.edu --recv-key 0x337EE704693C17EF \  
&& gpg --verify /tmp/s6-overlay-amd64.tar.gz.sig /tmp/s6-overlay-amd64.tar.gz
\  
&& rm -rf /root/.gnupg \  
  
# Install  
&& tar xvfz /tmp/s6-overlay-amd64.tar.gz -C / && rm -f /tmp/*  
  
##  
## INIT  
##  
ENTRYPOINT ["/init"]

