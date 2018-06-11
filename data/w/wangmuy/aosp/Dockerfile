FROM ubuntu:16.04  
MAINTAINER Zhongdi Wang <wangmuy@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Bash instead of Dash  
RUN echo "dash dash/sh boolean false" | debconf-set-selections && \  
dpkg-reconfigure -p critical dash  
  
# apt using ustc mirror  
COPY sources.ustc.list /etc/apt/sources.list  
  
RUN apt-get update  
  
# workaround for make 3.81/3.82  
RUN apt-get install -y wget && \  
wget http://mirrors.ustc.edu.cn/ubuntu/pool/main/m/make-
dfsg/make_3.81-8.2ubuntu3_amd64.deb -O /tmp/make.deb && \  
dpkg -i /tmp/make.deb  
  
RUN apt-get install -y git gnupg flex bison gperf build-essential sudo \  
zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \  
libncurses5-dev lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev
ccache \  
libgl1-mesa-dev libxml2-utils xsltproc unzip python \  
vim subversion dos2unix bc expect lzop && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:openjdk-r/ppa && apt-get update && apt-get install
-y --allow-unauthenticated openjdk-7-jdk openjdk-8-jdk  
# RUN add-apt-repository -y ppa:webupd8team/java && apt-get update && echo
oracle-java6-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && apt-get install -y oracle-java6-installer  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# All builds will be done by user aosp  
COPY gitconfig /root/.gitconfig  
COPY ssh_config /root/.ssh/config  
  
# Improve rebuild performance by enabling compiler cache  
ENV USE_CCACHE 1  
ENV CCACHE_DIR /tmp/ccache  
  
# chinese env  
ENV LANG C.UTF-8  
COPY . /scripts  
ENTRYPOINT ["/scripts/docker_entrypoint.sh"]  
  

