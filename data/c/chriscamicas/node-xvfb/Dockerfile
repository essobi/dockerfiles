FROM node:8  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV BUILD_DEPS="clang libdbus-1-dev libgtk2.0-dev libnotify-dev libgnome-
keyring-dev libgconf2-dev libasound2-dev libcap-dev libcups2-dev libxtst-dev
libnss3-dev"  
  
RUN echo "deb http://httpredir.debian.org/debian jessie main contrib non-free"
\  
> /etc/apt/sources.list \  
&& echo "deb http://httpredir.debian.org/debian jessie-updates main contrib
non-free" \  
>> /etc/apt/sources.list \  
&& echo "deb http://security.debian.org/ jessie/updates main contrib non-free"
\  
>> /etc/apt/sources.list \  
&& echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true" \  
| debconf-set-selections \  
&& apt-get update -qq \  
# this is needed so that everything is setup before.  
&& apt-get install -y apt-utils \  
&& apt-get install -y \  
$BUILD_DEPS \  
gcc-multilib \  
g++-multilib \  
xvfb \  
x11-xkb-utils \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-scalable \  
xfonts-cyrillic \  
x11-apps \  
fontconfig-config \  
xauth \  
libxss1 \  
\--no-install-recommends \  
&& apt-get remove -y $BUILD_DEPS \  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["node"]  

