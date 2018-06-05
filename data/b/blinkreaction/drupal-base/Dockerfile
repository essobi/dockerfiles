FROM buildpack-deps:jessie-curl  
  
MAINTAINER Leonid Makarov <leonid.makarov@blinkreaction.com>  
  
# Prevent services autoload (http://jpetazzo.github.io/2013/10/06/policy-rc-d-
do-not-start-services-automatically/)  
RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d && chmod +x
/usr/sbin/policy-rc.d  
  
# Enabling additional repos  
RUN sed -i 's/main/main contrib non-free/' /etc/apt/sources.list  
  
# Basic packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes --no-install-recommends
install \  
apt-transport-https \  
locales \  
supervisor \  
procps \  
mc \  
dnsutils \  
# Cleanup  
&& DEBIAN_FRONTEND=noninteractive apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set timezone and locale  
RUN dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
# Install gosu and give access to the users group to use it. gosu will be used
to run services as a different user.  
RUN curl -sSL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture)" -o /usr/local/bin/gosu && \  
chown root:users /usr/local/bin/gosu && \  
chmod +sx /usr/local/bin/gosu  
  
# Set TERM so text editors/etc. can be used  
ENV TERM xterm  

