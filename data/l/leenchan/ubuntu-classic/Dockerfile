FROM ubuntu:xenial  
MAINTAINER CUI Wei <ghostplant@qq.com>  
  
ENV LANG=en_US.UTF-8  
ENV INIT_PASS=_123456_  
ENV GEOMETRY=1024x768  
ENV SESSION=docker  
  
RUN bash -c "echo -e 'deb http://ppa.launchpad.net/ghostplant/flashback/ubuntu
xenial main' > /etc/apt/sources.list.d/ghostplant-ubuntu-flashback-
xenial.list"  
RUN apt-get update && apt-get install ca-certificates openssh-server htop
vnc4server xfonts-base debian-properties-common gnome-flashback-classic fcitx
fcitx-googlepinyin fcitx-ui-classic fcitx-frontend-gtk3 fcitx-config-gtk
language-pack-zh-hans language-pack-gnome-zh-hans libcurl3 firefox firefox-
locale-zh-hans dnsutils curl sudo psmisc gdebi-core iputils-ping rsync netcat-
openbsd whiptail bash-completion openssh-client p7zip-full iproute2 net-tools
vim-tiny openssl novnc-ex --allow-unauthenticated -y --no-install-recommends
&& apt-clean  
RUN rm -f /etc/apt/sources.list.d/ghostplant-ubuntu-flashback-xenial.list  
  
RUN bash -c "echo -e 'set backspace=indent,eol,start\nset nocompatible\nset
ts=4' >> /etc/vim/vimrc.tiny; echo '. /etc/bash_completion' >> /etc/profile"  
RUN update-flash-player  
  
RUN sed -Ei -e 's/^#?PermitRootLogin.*/PermitRootLogin yes/' -e
's/^#?UsePAM.*/UsePAM yes/' /etc/ssh/sshd_config  
  
# VOLUME ["/root"]  
EXPOSE 5901/tcp 8443/tcp  
  
CMD ["sh", "-c", "/bin/echo -e \"${INIT_PASS}\\\n${INIT_PASS}\" | vncpasswd &&
/bin/echo -e \"${INIT_PASS}\\\n${INIT_PASS}\" | chpasswd && /etc/init.d/ssh
restart && start-xvnc"]  
  

