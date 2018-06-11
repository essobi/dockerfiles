FROM ubuntu:trusty  
MAINTAINER Ian Blenke <ian@blenke.com>  
  
## Install latest trusty wine  
RUN apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common
&& \  
sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty main restricted
universe multiverse' /etc/apt/sources.list && \  
sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty-updates main
restricted universe multiverse' /etc/apt/sources.list && \  
sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty-backports main
restricted universe multiverse' /etc/apt/sources.list && \  
sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty-security main
restricted universe multiverse' /etc/apt/sources.list && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common
&& \  
sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty main restricted
universe multiverse' /etc/apt/sources.list && \  
add-apt-repository -y ppa:ubuntu-wine/ppa && \  
dpkg --add-architecture i386 && \  
apt-get update -y && \  
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true | sudo debconf-set-selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wine1.7 winetricks xvfb xrdp
xfce4-session xfce4 ca-certificates lib32gcc1 curl unzip tightvncserver && \  
apt-get autoclean -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add winetricks  
RUN wget -O /usr/local/bin/winetricks http://kegel.com/wine/winetricks  
RUN chmod 755 /usr/local/bin/winetricks  
  
# Add run.sh script  
ADD run.sh /run.sh  
  
EXPOSE 3389  
  
CMD /run.sh  

