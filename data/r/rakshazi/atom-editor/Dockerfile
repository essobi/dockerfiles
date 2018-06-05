FROM ubuntu:latest  
  
ENV TERM=xterm  
ENV ATOM_PACKAGES="file-icons remote-sync terminal-plus atom-autocomplete-php
docblockr linter linter-php php-fmt"  
RUN apt-get -qq update && \  
apt-get -qq install php7.0-cli \  
git \  
curl \  
ca-certificates \  
libgtk2.0-0 \  
libxtst6 \  
libnss3 \  
libgconf-2-4 \  
libasound2 \  
fakeroot \  
gconf2 \  
gconf-service \  
libcap2 \  
libnotify4 \  
libxtst6 \  
libnss3 \  
gvfs-bin \  
xdg-utils \  
composer \  
python -qq -y --allow-unauthenticated --no-install-recommends && \  
apt-get clean && \  
curl -L https://atom.io/download/deb > /tmp/atom.deb && \  
dpkg -i /tmp/atom.deb && \  
rm -f /tmp/atom.deb && \  
apm install ${ATOM_PACKAGES} && \  
apm rebuild ${ATOM_PACKAGES}  
  
RUN curl -L
https://github.com/phpfmt/releases/raw/master/releases/lts/803.3/fmt.phar >
/root/fmt.phar  
COPY config.cson /root/.atom/config.cson  
VOLUME /workspace  
CMD ["/usr/bin/atom","-f", "/workspace"]  

