FROM ubuntu:18.04  
  
MAINTAINER Bryce Anglin, <brycea@rapidnetworks.org>  
# Install Dependencies  
  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y software-properties-common \  
&& apt-get update \  
&& apt-get install -y \--install-recommends ca-certificates apt-utils wine64
winetricks libntlm0 wget \  
# Download wine cache files  
&& mkdir -p /home/container/.cache/wine \  
&& wget https://dl.winehq.org/wine/wine-mono/4.7.1/wine-mono-4.7.1.msi \  
-O /home/container/.cache/wine/wine-mono-4.7.1.msi \  
&& wget https://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86.msi \  
-O /home/container/.cache/wine/wine_gecko-2.47-x86.msi \  
&& wget https://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86_64.msi
\  
-O /home/container/.cache/wine/wine_gecko-2.47-x86_64.msi \  
# Download winetricks and cache files  
&& wget
https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
\  
-O /usr/bin/winetricks \  
&& chmod +rx /usr/bin/winetricks \  
&& mkdir -p /home/container/.cache/winetricks/win7sp1 \  
&& wget
https://download.microsoft.com/download/0/A/F/0AFB5316-3062-494A-AB78-7FB0D4461357/windows6.1-KB976932-X86.exe
\  
-O /home/container/.cache/winetricks/win7sp1/windows6.1-KB976932-X86.exe \  
# Create user and take ownership of files  
&& useradd -m -d /home/container container \  
&& chown -R container:container /home/container  
  
  
USER container  
ENV HOME /home/container  
ENV WINEARCH win64  
ENV WINEPREFIX /home/container/.wine64  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]  

