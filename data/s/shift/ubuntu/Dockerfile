FROM ubuntu:16.04  
  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
ADD files/01_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc  
  
ENV LANG en_GB.UTF-8  
ENV LANGUAGE en_GB:en  
ENV LC_ALL en_GB.UTF-8  
  
RUN rm -rf /usr/share/doc/* \  
&& locale-gen en_GB.UTF-8 \  
&& rm -rf
/usr/share/{doc,man,groff,info,lintian,linda,locale/de,locale/es,locale/ja,locale/fr,locale/zh}/*
\  
&& apt-get update \  
&& apt-get upgrade --yes \  
&& apt-get install --yes\  
&& for package in `dpkg --get-selections | grep -v libc-bin | grep -v
deinstall | cut -f 1`; do echo "Reconfigure $package"; dpkg-reconfigure -plow
$package; done \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
ONBUILD RUN apt-get update \  
&& apt-get upgrade --force-yes \--yes \  
&& apt-get install --force-yes \--yes software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  

