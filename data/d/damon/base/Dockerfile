# damon/base  
#  
# This sets up the base Ubuntu machine. It sets the locale, upgrades Ubuntu,  
# and installs some necessary packages.  
FROM ubuntu:14.04  
# Speed up apt-get  
RUN echo force-unsafe-io > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
  
# Update, then set the locale  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive locale-gen en_US.UTF-8 && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y --no-install-
recommends  
  
# Fix some issues with APT packages.  
# See https://github.com/dotcloud/docker/issues/1024  
RUN dpkg-divert --local \--rename --add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl  
  
# Required packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
curl \  
git \  
python-software-properties \  
software-properties-common && \  
rm -rf /var/lib/apt/lists/*  
  
# Helpful alias for attached sessions  
RUN echo 'alias l="ls -alh"' >> /etc/bash.bashrc  
  
# Default to bash  
CMD ["/bin/bash"]  
  
ONBUILD RUN apt-get update  

