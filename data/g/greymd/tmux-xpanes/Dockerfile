FROM debian:jessie-slim  
MAINTAINER Yamada, Yasuhiro <greengregson@gmail.com>  
  
# ------------------  
# Install Basic softwares  
# ------------------  
RUN echo 'deb
http://download.opensuse.org/repositories/shells:/fish:/release:/2/Debian_8.0/
/' > /etc/apt/sources.list.d/fish.list && \  
apt update && \  
apt install -y locales && \  
localedef -f UTF-8 -i ja_JP ja_JP.utf8 && \  
apt install -y git vim curl gcc make netcat nkf bc expect tree fish inotify-
tools  
  
# ------------------  
# Install Tmux related softwares  
# ------------------  
RUN apt-get install -y libevent-dev ncurses-dev && \  
export TMUX_VERSION=2.4 && \  
curl -L
"https://github.com/tmux/tmux/releases/download/${TMUX_VERSION}/tmux-${TMUX_VERSION}.tar.gz"
| tar zxv && \  
cd tmux-${TMUX_VERSION} && \  
curl -L
https://raw.githubusercontent.com/silenvx/PKGBUILD/master/tmux/borders.patch >
borders.patch && \  
patch tty-acs.c < borders.patch && \  
./configure; make && \  
make install && \  
cd .. && rm -rf tmux-${TMUX_VERSION} && \  
git clone https://github.com/tmux-plugins/tpm $HOME/.tmux/plugins/tpm  
  
# ------------------  
# Install xpanes  
# ------------------  
RUN curl https://raw.githubusercontent.com/greymd/tmux-
xpanes/master/bin/xpanes > /usr/bin/xpanes && \  
chmod +x /usr/bin/xpanes  
  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
# ------------------  
# Cleaning  
# ------------------  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

