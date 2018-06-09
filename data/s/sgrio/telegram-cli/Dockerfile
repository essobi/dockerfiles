FROM sgrio/ubuntu-python:2  
  
RUN \  
DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
git \  
luajit \  
luarocks \  
libreadline-dev \  
libconfig-dev \  
libssl-dev \  
lua5.2 \  
liblua5.2-dev \  
libevent-dev \  
libjansson-dev \  
libpython-dev && \  
git clone --recursive https://github.com/vysheng/tg.git /tg && \  
cd /tg && ./configure && make && \  
mkdir -p /usr/local/share/telegram-cli/bin && \  
mv -v /tg/bin/* /usr/local/share/telegram-cli/bin/ && \  
ln -sf /usr/local/share/telegram-cli/bin/generate /usr/bin/ && \  
ln -sf /usr/local/share/telegram-cli/bin/generate /usr/local/bin/ && \  
ln -sf /usr/local/share/telegram-cli/bin/telegram-cli /usr/bin/ && \  
ln -sf /usr/local/share/telegram-cli/bin/telegram-cli /usr/local/bin/ && \  
ln -sf /usr/local/share/telegram-cli/bin/tl-parser /usr/bin/ && \  
ln -sf /usr/local/share/telegram-cli/bin/tl-parser /usr/local/bin/ && \  
mkdir -p /etc/telegram-cli/ && \  
mv -v /tg/tg-server.pub /etc/telegram-cli/server.pub && \  
pip install pytg --no-cache-dir && \  
apt-get purge -y --auto-remove \  
build-essential \  
git && \  
apt-get autoclean && apt-get autoremove --purge -y && \  
rm -rf \  
/tg \  
/var/lib/apt/lists/* \  
/var/cache/apt/* \  
/tmp/* \  
/var/tmp/*  
  

