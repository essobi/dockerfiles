FROM ubuntu:bionic  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN echo "APT::Acquire::Retries=16;" >> /etc/apt/apt.conf.d/99_retries  
RUN apt-get update  
RUN apt-get install -y --fix-missing sudo apt-utils aptitude dirmngr  
RUN apt-get -y upgrade  
  
RUN apt-get -y install whois zsh tmux atop aria2 curl pv nodejs npm python-dev
ruby-dev dkms linux-kernel-headers golang  
RUN apt-get -y --fix-missing install lm-sensors mercurial git  
RUN apt-get -y --fix-missing install build-essential cmake intltool  
RUN apt-get -y --fix-missing install xorg  
RUN apt-get -y --fix-missing install meld  
RUN apt-get -y --fix-missing install gajim  
RUN apt-get -y --fix-missing install lm-sensors  
RUN apt-get -y --fix-missing install terminator  
RUN apt-get -y --fix-missing install python3-pip python-pip  
RUN apt-get -y --fix-missing install freecad  
RUN apt-get -y --fix-missing install keepass2  
RUN apt-get -y --fix-missing install libncurses5-dev libgnome2-dev libgnomeui-
dev libgtk2.0-dev libatk1.0-dev libbonoboui2-dev libcairo2-dev libx11-dev
libxpm-dev libxt-dev  
RUN apt-get -y --fix-missing install gsmartcontrol redshift gtk-redshift
gparted solaar glances silversearcher-ag retext kdiff3  
RUN mkdir -p /root/dev/  
# vim  
RUN git clone https://github.com/vim/vim.git --recursive /root/dev/vim  
RUN cd /root/dev/vim && ./configure --with-features=huge \  
\--enable-multibyte \  
\--enable-rubyinterp \  
\--enable-python3interp=yes \  
\--enable-luainterp \  
\--enable-gui=no \  
\--enable-cscope  
RUN cd /root/dev/vim && make -j`nproc`  
RUN cd /root/dev/vim && sudo make install  
  
RUN curl -sSf https://sh.rustup.rs > /tmp/rustup  
RUN chmod a+x /tmp/rustup  
RUN /tmp/rustup -y  
RUN rm -f /tmp/rustup  
RUN /root/.cargo/bin/rustup update  
RUN /root/.cargo/bin/rustup default stable  
RUN /root/.cargo/bin/cargo install racer  
RUN /root/.cargo/bin/cargo install rustsym  
RUN /root/.cargo/bin/cargo install ripgrep  
RUN /root/.cargo/bin/cargo install just  
RUN /root/.cargo/bin/cargo install cargo-update  
  

