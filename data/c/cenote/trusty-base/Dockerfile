FROM ubuntu:14.04  
  
RUN set -e && \  
apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
# ttf-mscorefonts-installer has often problems with font download. Checking
this first and exit on fail  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections && \  
apt-get update && apt-get install -y --no-install-recommends ttf-mscorefonts-
installer 2>&1 | tee fontinstall.log |cat && \  
if grep -q Traceback fontinstall.log ; then echo "Error on font download!" ;
exit 1; fi && rm fontinstall.log  
  
# Basic things  
RUN set -e && \  
apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
fontconfig \  
git \  
lib32z1 \  
openssh-client \  
software-properties-common \  
wget \  
lib32ncurses5 \  
&& rm -rf /var/lib/apt/lists/*  
# nsis  
RUN set -e && \  
dpkg --add-architecture i386 && \  
apt-get update && apt-get install -y --no-install-recommends \  
libstdc++6:i386 \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD nsis-2.46-linux32-bin.tar.bz2 /opt  
ENV PATH /opt/nsis-2.46/bin:$PATH  

