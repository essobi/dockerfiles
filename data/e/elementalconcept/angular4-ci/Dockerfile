FROM ubuntu:xenial  
  
# Generic dependencies  
RUN apt-get update -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apt-transport-https curl
bzip2 xz-utils  
  
# Installing Node.js v8.6.0  
RUN curl https://nodejs.org/dist/v8.6.0/node-v8.6.0-linux-x64.tar.xz >
/root/node-v8.6.0-linux-x64.tar.xz  
RUN tar xf /root/node-v8.6.0-linux-x64.tar.xz -C /root  
RUN ln -s /root/node/bin/node /usr/bin/node  
RUN ln -s /root/node/bin/npm /usr/bin/npm  
# Clean-up  
RUN mv /root/node-v8.6.0-linux-x64 /root/node  
RUN rm /root/node-v8.6.0-linux-x64.tar.xz  
  
# Installing Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -y
yarn  
  
# Installing Xorg with a dummy driver  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y xserver-xorg-video-dummy  
ADD assets/xorg.conf /root/xorg.conf  
  
# Installing Chromium  
RUN mkdir /home/chrome  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y chromium-browser  
RUN mv /usr/bin/chromium-browser /usr/bin/chromium-browser-bin  
ADD assets/chromium-browser /usr/bin/chromium-browser  
RUN chmod +x /usr/bin/chromium-browser  
RUN export CHROME_BIN=chromium-browser  
  
# We don't need MS fonts yet, but it was pain the arse to install them
correctly, so let's keep this snippet here  
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget cabextract  
# RUN curl http://ftp.uk.debian.org/debian/pool/contrib/m/msttcorefonts/ttf-
mscorefonts-installer_3.6_all.deb > /root/ttf-mscorefonts-
installer_3.6_all.deb  
# RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections  
# RUN dpkg -i /root/ttf-mscorefonts-installer_3.6_all.deb  

