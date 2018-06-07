# docker run -it --rm -v /tmp:/tmp liyin/tmux  
  
FROM ubuntu:latest  
MAINTAINER Li Yin <liyin@live.com>  
ADD 0001-Revert-back-7382ba8-to-add-back-italic-support.patch /root/  
RUN cd /root && sed -i 's/^# deb-src/deb-src/g' /etc/apt/sources.list && \  
sed -i 's/archive.ubuntu.com/mirror.0x.sg/g' /etc/apt/sources.list && \  
apt-get update && apt-get -y install git && apt-get build-dep -y tmux && \  
git clone https://github.com/tmux/tmux.git && cd tmux && ./autogen.sh && \  
git config user.email liyin@live.com && git config user.name liyin && \  
git am /root/*.patch && ./configure --prefix=/usr/local && make -j29 && \  
apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  

