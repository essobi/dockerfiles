FROM python:3.5  
MAINTAINER Christian Meter <meter@cs.uni-duesseldorf.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV src /etc/apt/sources.list  
ENV locs /etc/locale.gen  
  
# Remove old sources.list  
RUN mv $src $src.bak && \  
touch $src  
  
# Add local mirrors  
RUN echo "deb http://mirror.cs.uni-duesseldorf.de/debian/ jessie main contrib
non-free" >> $src && \  
echo "deb-src http://mirror.cs.uni-duesseldorf.de/debian/ jessie main contrib
non-free" >> $src && \  
echo "deb http://httpredir.debian.org/debian jessie main" >> $src && \  
echo "deb http://httpredir.debian.org/debian jessie-updates main" >> $src && \  
echo "deb http://security.debian.org/ jessie/updates main contrib non-free" >>
$src && \  
echo "deb-src http://security.debian.org/ jessie/updates main contrib non-
free" >> $src  
  
# Install packages  
RUN apt-get update -qq && \  
apt-get install -qqy locales libsasl2-dev python-dev libldap2-dev libssl-dev  
  
# Create locales  
RUN mv $locs $locs.bak && \  
touch $locs && \  
echo "de_DE.UTF-8 UTF-8" >> $locs && \  
echo "en_US.UTF-8 UTF-8" >> $locs && \  
locale-gen  
  
# Set language  
ENV LANG de_DE.UTF-8  

