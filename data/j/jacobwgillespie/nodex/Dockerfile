FROM node:6  
  
RUN \  
# Update packages  
apt-get update -qq && \  
# Install dependencies  
apt-get install -qy \  
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
g++-multilib && \  
# Make app dir  
mkdir -p /app && \  
# Cleanup  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/* /root/sources/*  
  
COPY entrypoint /entrypoint  
WORKDIR /app  
ENTRYPOINT ["/entrypoint"]  
CMD ["node"]  

