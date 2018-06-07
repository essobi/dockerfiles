FROM debian:stretch  
  
  
# Add components used for the GUI  
RUN apt-get update && apt-get install -y \  
libasound2 \  
libatk1.0-0 \  
libcairo2 \  
libcups2 \  
libdatrie1 \  
libdbus-1-3 \  
libfontconfig1 \  
libfreetype6 \  
libgconf-2-4 \  
libgcrypt20 \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libgdk-pixbuf2.0-0 \  
libglib2.0-0 \  
libgpg-error0 \  
libgraphite2-3 \  
libnotify-bin \  
libnss3 \  
libnspr4 \  
libpango-1.0-0 \  
libpangocairo-1.0-0 \  
libxcomposite1 \  
libxcursor1 \  
libxdmcp6 \  
libxi6 \  
libxrandr2 \  
libxrender1 \  
libxss1 \  
libxtst6 \  
liblzma5 \  
libxkbfile1 \  
sudo \  
gnupg \  
wget \  
ttf-bitstream-vera \  
pulseaudio \  
lxappearance \  
locales  
  
#Tell that I speak English  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
a&& /usr/sbin/update-locale LANG=en_US.UTF-8  
#Add emoji  
RUN wget https://github.com/eosrei/emojione-color-
font/releases/download/v1.3/fonts-emojione-svginot_1.3-1_all.deb &&\  
dpkg -i fonts-emojione-svginot_1.3-1_all.deb &&\  
rm -f fonts-emojione-svginot_1.3-1_all.deb  
  
# Improve font rendering  
RUN echo "deb http://ppa.launchpad.net/no1wantdthisname/ppa/ubuntu xenial
main" >>/etc/apt/sources.list &&\  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E985B27B &&\  
apt-get update &&\  
apt-get install -y fontconfig-infinality &&\  
bash /etc/fonts/infinality/infctl.sh setstyle infinality  
  
# Add my x-browser-forwarder  
RUN wget https://github.com/meyskens/x-www-browser-
forward/releases/download/0.0.1/client && \  
mv client /etc/alternatives/x-www-browser && \  
chmod +x /etc/alternatives/x-www-browser && \  
ln -s /etc/alternatives/x-www-browser /usr/bin/x-www-browser  
  
#Add user for apps that do not support root  
RUN useradd user && usermod -aG sudo user  
RUN mkdir /home/user && chown -R user /home/user  
RUN echo "ALL ALL = (ALL) NOPASSWD: ALL" >>/etc/sudoers  

