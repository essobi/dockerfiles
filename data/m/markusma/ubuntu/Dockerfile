# Ubuntu Trusty base image with updates, fixes and useful packages installed.  
FROM ubuntu:trusty  
MAINTAINER Markus Mattinen <markus@gamma.fi>  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty main restricted
universe multiverse" > /etc/apt/sources.list \  
&& echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-updates main
restricted universe multiverse" >> /etc/apt/sources.list \  
&& echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-security main
restricted universe multiverse" >> /etc/apt/sources.list \  
&& echo "deb-src mirror://mirrors.ubuntu.com/mirrors.txt trusty main
restricted universe multiverse" >> /etc/apt/sources.list \  
&& echo force-unsafe-io > /etc/dpkg/dpkg.cfg.d/02apt-speedup \  
&& echo udev hold | dpkg \--set-selections \  
&& echo initscripts hold | dpkg \--set-selections \  
&& echo upstart hold | dpkg \--set-selections \  
&& dpkg-divert \--local \--rename \--add /sbin/start \  
&& dpkg-divert \--local \--rename \--add /sbin/initctl \  
&& dpkg-divert \--local \--rename \--add /usr/bin/ischroot \  
&& dpkg-divert \--local \--rename \--add /usr/bin/chfn \  
&& ln -sf /bin/true /sbin/start \  
&& ln -sf /bin/true /sbin/initctl \  
&& ln -sf /bin/true /usr/bin/ischroot \  
&& ln -sf /bin/true /usr/bin/chfn \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends apt-transport-https \  
&& apt-get install -y \--no-install-recommends language-pack-en curl wget vim
software-properties-common git-core \  
&& apt-get dist-upgrade -y \--no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& echo "LANG=en_US.UTF-8" > /etc/default/locales \  
&& echo "LC_COLLATE=en_US.UTF-8" >> /etc/default/locales \  
&& echo "LC_CTYPE=en_US.UTF-8" >> /etc/default/locales \  
&& echo "LC_MESSAGES=en_US.UTF-8" >> /etc/default/locales \  
&& echo "LC_MONETARY=en_US.UTF-8" >> /etc/default/locales \  
&& echo "LC_NUMERIC=en_US.UTF-8" >> /etc/default/locales \  
&& echo "LC_PAPER=en_US.UTF-8" >> /etc/default/locales \  
&& echo "LC_NAME=en_US.UTF-8" >> /etc/default/locales \  
&& echo "LC_ADDRESS=en_US.UTF-8" >> /etc/default/locales \  
&& echo "LC_TELEPHONE=en_US.UTF-8" >> /etc/default/locales \  
&& echo "LC_MEASUREMENT=en_US.UTF-8" >> /etc/default/locales \  
&& echo "LC_IDENTIFICATION=en_US.UTF-8" >> /etc/default/locales \  
&& echo "LC_TIME=en_US.UTF-8" >> /etc/default/locales  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN dpkg-reconfigure locales  

