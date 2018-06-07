FROM debian:latest  
RUN apt-get -y update && \  
apt-get -y install subversion build-essential libncurses5-dev zlib1g-dev gawk
git ccache gettext libssl-dev xsltproc wget fakeroot \  
unzip gawk subversion mercurial \  
libgnutls28-dev bsdmainutils \  
lua5.1 lua-cjson lua-socket luarocks qrencode && \  
luarocks install busted && \  
rm -rf /var/lib/apt/lists/*  
COPY install /tmp/install  
RUN /bin/sh /tmp/install/install.sh && rm -rf /tmp/install  

