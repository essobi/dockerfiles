FROM python:2  
MAINTAINER boh.ricky  
  
# install deb  
RUN rm -f -r /etc/apt/sources.list && \  
wget -O /etc/apt/sources.list http://mirrors.163.com/.help/sources.list.jessie
&& \  
apt-get update && \  
apt-get install -y lua5.2 liblua5.2-dev && \  
cd /tmp && \  
# build and install vim  
git clone https://github.com/vim/vim.git && \  
cd vim && \  
./configure --with-features=huge --enable-luainterp \  
\--enable-gui=no \--without-x \--prefix=/usr && \  
make VIMRUNTIMEDIR=/usr/share/vim/vim74 && \  
make install && \  
# spf13  
curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh && \  
# cleanup  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

