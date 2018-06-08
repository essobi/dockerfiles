FROM clarkchen633/ubuntux64:17.04  
MAINTAINER clarkchen633 <clarkchen633@gmail.com>  
  
# Allow replacing httpredir mirror  
ARG APT_MIRROR=httpredir.debian.org  
ENV TZ=Asia/Taipei  
  
# Add deb-src lines to make apt-get build-dep work.  
RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d \  
&& sed -i s/httpredir.debian.org/$APT_MIRROR/g /etc/apt/sources.list \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
\  
&& apt-get update \  
&& apt-get update && apt-get install -y \--no-install-recommends apt-utils
apt-file \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y vim.tiny wget sudo net-
tools ca-certificates unzip apt-transport-https curl \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  

