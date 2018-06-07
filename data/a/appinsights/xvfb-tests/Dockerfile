FROM node:6-slim  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
COPY start /usr/local/bin/start-xvfb  
  
RUN chmod +x /usr/local/bin/start-xvfb  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'  
  
RUN wget mozilla.debian.net/pkg-mozilla-archive-keyring_1.1_all.deb \  
&& dpkg -i pkg-mozilla-archive-keyring_1.1_all.deb \  
&& sh -c 'echo "deb http://security.debian.org/ jessie/updates main" >>
/etc/apt/sources.list.d/firefox.list' \  
&& rm -f pkg-mozilla-archive-keyring_1.1_all.deb  
  
RUN apt update -qq && \  
apt install -y \  
google-chrome-stable \  
firefox-esr \  
xvfb \  
x11-xkb-utils \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-scalable \  
xfonts-cyrillic \  
x11-apps \  
clang \  
libdbus-1-dev \  
libgtk2.0-dev \  
libnotify-dev \  
libgnome-keyring-dev \  
libgconf2-dev \  
libasound2-dev \  
libcap-dev \  
libcups2-dev \  
libxtst-dev \  
libxss1 \  
libnss3-dev \  
gcc-multilib \  
g++-multilib \  
xauth \  
git \  
sudo \  
\--no-install-recommends \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/api/lists/*  
  

