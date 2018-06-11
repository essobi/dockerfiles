FROM ubuntu:14.04  
MAINTAINER Tobias Mandjik "webmaster@leckerbeef.de"  
# ORIGINAL MAINTAINER Felix Bartels "felix@host-consultants.de"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq -y \  
&& apt-get install -qq -y wget \  
&& mkdir -p /root/packages \  
&& cd /root/packages \  
&& wget -q
http://download.zarafa.com/zarafa/drupal/download_platform.php?platform=beta/7.1/7.1.14RC1-51758/zcp-7.1.14RC1-51758-ubuntu-14.04-x86_64-forhome.tar.gz
-O- | tar xz --strip-components=1 \  
&& apt-ftparchive packages . | gzip -9c > Packages.gz \  
&& echo "deb file:/root/packages /" > /etc/apt/sources.list.d/zarafa.list \  
&& apt-get update -qq -y \  
&& apt-get install -qq -y \--force-yes mysql-server zarafa \  
&& apt-get clean  

