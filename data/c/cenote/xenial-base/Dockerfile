FROM ubuntu:16.04  
# Ubuntu release name  
ENV URELEASE xenial  
  
# Basic things  
RUN set -e && \  
apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https \  
ca-certificates \  
curl \  
fontconfig \  
git \  
openssh-client \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -e && umask 077 && mkdir -p ~/.ssh  
  
# ttf-mscorefonts-installer needs now apt-transport-https which has to be
installed before  
# ttf-mscorefonts-installer has often problems with font download. Checking
this first and exit on fail  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ ${URELEASE} multiverse" >>
/etc/apt/sources.list && \  
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true | debconf-set-selections && \  
apt-get update && apt-get install -y --no-install-recommends \  
ttf-mscorefonts-installer 2>&1 | tee fontinstall.log && \  
if grep -q Traceback fontinstall.log ; then echo "Error on font download!" ;
exit 1; fi && rm fontinstall.log  
  
# nsis  
RUN set -e && \  
dpkg --add-architecture i386 && \  
apt-get update && apt-get install -y --no-install-recommends \  
libstdc++6:i386 \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD nsis-2.46-linux32-bin.tar.bz2 /opt  
ENV PATH /opt/nsis-2.46/bin:$PATH  

