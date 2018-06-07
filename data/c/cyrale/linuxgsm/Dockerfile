FROM ubuntu:16.04  
# Stop apt-get asking to get Dialog frontend  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# Install dependencies and clean  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y \  
binutils \  
bsdmainutils \  
bzip2 \  
curl \  
file \  
git \  
gzip \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
libc6 \  
libstdc++6 \  
libstdc++6:i386 \  
mailutils \  
postfix \  
python \  
tmux \  
util-linux \  
unzip \  
wget && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
# Add the steam user  
RUN adduser \  
\--disabled-login \  
\--disabled-password \  
\--shell /bin/bash \  
steam  
  
# Select the script as entry point  
COPY ./update-linuxgsm.sh /home/steam/  
RUN [ -d /home/steam/linuxgsm ] || mkdir -p /home/steam/linuxgsm && \  
chown -R steam:steam /home/steam && \  
chmod u+x /home/steam/update-linuxgsm.sh  
  
# Switch to the user steam  
USER steam  
  
# Download and extract steamcmd  
RUN git clone "https://github.com/GameServerManagers/LinuxGSM.git"
/home/steam/linuxgsm && \  
cd /home/steam/linuxgsm && \  
git checkout legacy  
  
CMD ["/home/steam/update-linuxgsm.sh"]  

