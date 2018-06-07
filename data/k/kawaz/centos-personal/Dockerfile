FROM kawaz/centos-ja  
MAINTAINER Yoshiaki Kawazu <kawazzz@gmail.com>  
  
# 作業用  
RUN yum list > /tmp/yum_list  
RUN yum -y install git tar unzip vim net-tools psmisc  
RUN git clone https://github.com/kawaz/dotfiles.git ~/.dotfiles  
RUN ~/.dotfiles/bin/setup.sh  
# NeoBundleInstalの為に一回起動して終了させる上手いやり方、求む  
RUN bash -ic '(sleep 150; killall -9 vim) & vim -c :q! - <<< ""; true'  

