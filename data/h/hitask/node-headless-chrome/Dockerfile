FROM node:8.9  
# Install basic tools/utilities and google Chrome unstable (which has cross
platform support for headless mode). Combining them together so that apt cache
cleanup would need to be done just once.  
RUN apt-get update -y && \  
apt-get install ca-certificates \  
gconf-service \  
libasound2 \  
libatk1.0-0 \  
libatk1.0-0 \  
libdbus-1-3 \  
libgconf-2-4 \  
libgtk-3-0 \  
libnspr4 \  
libnss3 \  
libx11-xcb1 \  
libxss1 \  
libxtst6 \  
fonts-liberation \  
libappindicator1 \  
xdg-utils \  
lsb-release \  
wget \  
curl \  
zip \  
xz-utils -y --no-install-recommends && \  
wget https://dl.google.com/linux/direct/google-chrome-
unstable_current_amd64.deb && \  
dpkg -i google-chrome*.deb && \  
apt-get install -f && \  
apt-get clean autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* google-chrome-
unstable_current_amd64.deb  

