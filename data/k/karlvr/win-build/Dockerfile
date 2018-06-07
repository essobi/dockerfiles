# WiX Toolset  
# Create Windows installation packages  
  
# Run WiX on Linux using Wine  
  
FROM ubuntu  
MAINTAINER Karl von Randow <karl@xk72.com>  
  
RUN apt-get update  
  
###############################################################################  
# MingW  
RUN apt-get install -y mingw-w64 mingw-w64-tools  
  
###############################################################################  
# osslsigncode  
  
# OpenSSL-based signcode utility  
  
# Platform-independent tool for Authenticode signing of PE(EXE/SYS/DLL/etc),  
# CAB and MSI files - uses OpenSSL and libcurl. It also supports  
# timestamping (Authenticode and RFC3161).  
  
# https://sourceforge.net/projects/osslsigncode/  
# https://sourceforge.net/p/osslsigncode/osslsigncode/ci/master/tree/  
# https://stackoverflow.com/a/29073957/1951952  
  
RUN apt-get update && apt-get install -y osslsigncode  
  
###############################################################################  
# WiX  
  
# Wine repository  
RUN dpkg --add-architecture i386 && \  
apt-get install -y wget apt-transport-https && \  
wget -nc https://dl.winehq.org/wine-builds/Release.key && \  
apt-key add Release.key && \  
echo "deb https://dl.winehq.org/wine-builds/ubuntu/ xenial main" >
/etc/apt/sources.list.d/winehq.list && \  
apt-get update  
  
# Install Wine  
RUN apt-get install -y winehq-stable  
  
# https://wiki.winehq.org/Winetricks  
RUN wget -O /usr/local/bin/winetricks
https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
&& \  
chmod +x /usr/local/bin/winetricks  
  
# Install WIX  
RUN apt-get install -y unzip && \  
mkdir -p /opt/wix && \  
wget -O /opt/wix/wix.zip
https://github.com/wixtoolset/wix3/releases/download/wix311rtm/wix311-binaries.zip
&& \  
cd /opt/wix && \  
unzip wix.zip && \  
rm wix.zip  
  
RUN apt-get install -y xauth ca-certificates  
  
RUN useradd --create-home --home /home/builder --groups users builder --shell
/bin/bash  
RUN mkdir /build  
  
USER builder  
WORKDIR /build  
  
# Setup Dotnet 4.0  
ENV WINEARCH=win32  
RUN /usr/local/bin/winetricks --unattended dotnet40  

