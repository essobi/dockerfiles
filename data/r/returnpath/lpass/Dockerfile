FROM ubuntu:14.04  
RUN set -x && \  
apt-get update && \  
apt-get clean  
  
ENV VER 0f9e3d9  
  
RUN set -x && \  
apt-get install -y openssl libcurl4-openssl-dev libxml2 libssl-dev \  
libxml2-dev pinentry-curses curl make unzip \  
build-essential git AsciiDoc cmake man jq && \  
git clone https://github.com/lastpass/lastpass-cli.git && \  
cd lastpass-cli && \  
git checkout ${VER} && \  
cmake . && make && make install && make install-doc && \  
cd / && rm -rf /lastpass-cli && \  
apt-get purge --auto-remove -y \  
libcurl4-openssl-dev libssl-dev libxml2-dev unzip \  
build-essential git AsciiDoc cmake && \  
apt-get clean  
  
RUN apt-get install -y gettext-base gawk && \  
apt-get clean  
  
ADD bin/* /usr/local/bin/  
  
VOLUME /root/.lpass  
  
ENTRYPOINT ["/usr/local/bin/lpass"]  

