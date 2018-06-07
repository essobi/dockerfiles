FROM ubuntu:14.04  
#ref  
#http://www.infoq.com/cn/articles/talk-about-docker-running-the-chinese-gui-
software  
MAINTAINER FanLin <linfan.china@gmail.com>  
MAINTAINER <github.com/wanjochan>  
  
# run in root mode  
USER root  
  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise main restricted
universe multiverse \n\  
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-updates main restricted
universe multiverse \n\  
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-backports main restricted
universe multiverse \n\  
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-security main restricted
universe multiverse" >> /etc/apt/sources.list  
  
#RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe\n" >
/etc/apt/sources.list && echo "deb http://archive.ubuntu.com/ubuntu trusty-
updates main universe\n" >> /etc/apt/sources.list  
RUN apt-get update -y  
  
# zh_CN  
ENV LANGUAGE zh_CN.UTF-8  
ENV LANG zh_CN.UTF-8  
ENV LC_ALL=zh_CN.UTF-8  
RUN /usr/share/locales/install-language-pack zh_CN && locale-gen zh_CN.UTF-8
&& dpkg-reconfigure --frontend noninteractive locales && apt-get -qqy --no-
install-recommends install language-pack-zh-hans  
  
# Basic Font  
RUN apt-get -y --no-install-recommends install fonts-ipafont-gothic
xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable  
  
# 文泉驿微米黑  
RUN apt-get -y install ttf-wqy-microhei && ln /etc/fonts/conf.d/65-wqy-
microhei.conf /etc/fonts/conf.d/69-language-selector-zh-cn.conf  
  
# Timezone  
ENV TZ "PRC"  
RUN echo "Asia/Hongkong" | tee /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
# Add User "vncuser" with passwd but can sudo. DANGER: must change pass after
run up.  
RUN useradd vncuser --shell /bin/bash --create-home && usermod -a -G sudo
vncuser && echo 'vncuser ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers && echo
'vncuser:vncpass' | chpasswd  
  
# basic tools  
RUN apt-get -y --no-install-recommends install curl wget bash \  
&& apt-get autoclean && apt-get autoremove && rm -rf /var/lib/apt/lists/*  
  

