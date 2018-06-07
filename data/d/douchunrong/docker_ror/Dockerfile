#################################################################  
# This docker image build file creates an image that contains  
# base rvm with ruby on rails.  
#  
# ## .  
# ## ## ## ==  
# ## ## ## ## ===  
# /""""""""""""""""\\___/ ===  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~  
# \\______ o __/  
# \ \ __/  
# \\____\\______/  
#  
# Component: RNTD  
# Author: Dou Chunrong <douchunrong@gmail.com>  
# Copyright: (c) 2015-2016 RNTD Ltd. All rights reserved.  
#################################################################  
#Version 0.0.1  
#RUBY 2.2-head  
FROM ubuntu:15.10  
  
#SIGN  
MAINTAINER Dou Chunrong <douchunrong@gmail.com>  
#更新源  
RUN apt-get update && apt-get upgrade -y  
  
#安装依赖工具  
RUN apt-get install -y --force-yes curl imagemagick-common libfftw3-double3
liblqr-1-0 libmagickcore-6-arch-config libmagickcore-6-headers libpng12-0
libxml2 libmagickcore-6.q16-2 libmagickwand-6.q16-2 mysql-common
libmysqlclient18 libpcrecpp0v5 libtiffxx5 libyaml-0-2 libc-ares2 libgssapi-
krb5-2 libkrb5-3 libkrb5support0 libk5crypto3 autoconf autotools-dev automake
bzip2-doc gir1.2-rsvg-2.0 git-core icu-devtools imagemagick-6.q16 imagemagick
libgssrpc4 libkdb5-8 libkadm5srv-mit9 libkadm5clnt-mit9 comerr-dev
krb5-multidev libbz2-dev libcairo-script-interpreter2 libexpat1-dev zlib1g-dev
libpng12-dev libfreetype6-dev libfontconfig1-dev xorg-sgml-doctools x11proto-
core-dev libxau-dev libxdmcp-dev x11proto-input-dev x11proto-kb-dev xtrans-dev
libpthread-stubs0-dev libxcb1-dev libx11-dev x11proto-render-dev libxrender-
dev x11proto-xext-dev libxext-dev libice-dev libsm-dev libpixman-1-dev libxcb-
render0-dev libxcb-shm0-dev libpcre32-3 libpcre3-dev libglib2.0-dev
libcairo2-dev libcdt5 libcgraph6 libjpeg-turbo8-dev libjpeg8-dev libjpeg-dev
libdjvulibre-dev libjs-jquery libexif-dev libgdk-pixbuf2.0-dev libpathplan4
libgvc6 libgvpr2 libxdot4 libltdl-dev libgraphviz-dev libicu-dev libilmbase12
libilmbase-dev libjasper-dev liblcms2-dev liblqr-1-0-dev libopenexr22
libmagickcore-6.q16-2-extra libopenexr-dev librsvg2-dev libjbig-dev liblzma-
dev libtiff5-dev libwmf-dev libxml2-dev libxt-dev libmagickcore-6.q16-dev
libmagickwand-6-headers libmagickwand-6.q16-dev libmagickwand-dev
libmysqlclient-dev libnetpbm10 libpq5 libssl-dev libpq-dev libtinfo-dev
libreadline6-dev libssl-doc libtool libv8-3.14.5 libx11-doc libxslt1-dev
netpbm libyaml-dev nodejs  
  
#设置ssh密码  
RUN apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd  
RUN echo "root:rntd12114" | chpasswd  
  
#安装JDK  
RUN apt-get install -y openjdk-7-jre  
RUN apt-get install -y openjdk-7-jdk  
  
#安装 rvm  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -c "source ~/.bashrc"  
  
#安装ruby  
RUN /bin/bash -l -c "rvm install ruby-2"  
RUN /bin/bash -l -c "rvm install ruby-2.2-head"  
RUN /bin/bash -l -c "rvm use 2.2-head --default"  
  
#安装rails  
RUN /bin/bash -l -c "gem install rails"  
  
#清理  
RUN apt-get clean  
  
#创建工作空间  
RUN mkdir /var/www  
  
#配置环境变量  
ENV PATH=$PATH:/usr/local/rvm/bin  
RUN echo '[[ -s "/usr/local/rvm/scripts/rvm" ]] && .
"/usr/local/rvm/scripts/rvm"' >> ~/.bashrc  
RUN /bin/bash -l -c " source ~/.bashrc "  
  
#开放端口  
EXPOSE 22 80  

