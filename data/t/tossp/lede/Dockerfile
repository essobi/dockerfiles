FROM ubuntu:trusty  
MAINTAINER TossPig "tse.code@TossP.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# RUN echo deb http://mirrors.163.com/ubuntu/ trusty main restricted universe
multiverse > /etc/apt/sources.list && \  
# echo deb http://mirrors.163.com/ubuntu/ trusty-security main restricted
universe multiverse >> /etc/apt/sources.list && \  
# echo deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted
universe multiverse >> /etc/apt/sources.list && \  
# echo deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted
universe multiverse >> /etc/apt/sources.list && \  
# echo deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted
universe multiverse >> /etc/apt/sources.list && \  
# echo deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe
multiverse >> /etc/apt/sources.list && \  
# echo deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted
universe multiverse >> /etc/apt/sources.list && \  
# echo deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted
universe multiverse >> /etc/apt/sources.list && \  
# echo deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted
universe multiverse >> /etc/apt/sources.list && \  
# echo deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted
universe multiverse >> /etc/apt/sources.list  
RUN apt-get -qqy update  
RUN apt-get -qqy install build-essential asciidoc binutils bzip2 gawk gettext
git libncurses5-dev libz-dev patch unzip zlib1g-dev lib32gcc1 libc6-dev-i386
subversion flex uglifyjs git-core gcc-multilib p7zip p7zip-full msmtp libssl-
dev texinfo libglib2.0-dev  
RUN apt-get -qqy install curl wget  
RUN apt-get -qqy install sudo bsdmainutils autoconf automake libtool tree  
RUN apt-get -qqy install gettext libattr1-dev  
RUN useradd -d /home/lede -m -s /bin/bash lede  

