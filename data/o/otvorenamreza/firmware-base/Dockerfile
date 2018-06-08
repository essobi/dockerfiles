FROM tozd/base:ubuntu-bionic  
  
ENV FW_PACKAGE_HOST packages.wlan-si.net  
  
RUN apt-get -q -q update && \  
apt-get \--no-install-recommends --yes --force-yes install \  
subversion g++ zlib1g-dev build-essential git python rsync man-db \  
libncurses5-dev gawk gettext unzip file libssl-dev wget zip time \  
ca-certificates fakeroot quilt curl && \  
useradd --home-dir /builder \--shell /bin/bash \--no-create-home builder  
  
WORKDIR /buildsystem  
ENV HOME /buildsystem  
ADD . /buildsystem  

