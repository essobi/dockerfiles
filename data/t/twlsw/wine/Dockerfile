FROM ubuntu:16.04  
MAINTAINER Towel Software <www.towel.dk>  
  
ENV LANG C.UTF-8  
USER root  
  
# Original script by Jan Suchotzki <jan@suchotzki.de>  
# from https://github.com/suchja/wix-toolset/blob/master/waitonprocess.sh  
RUN echo '[ $# -lt 2 ] && echo "Usage: $0 USER PROCESS-NAMES..." >&2 && exit 1
\n\  
USER="$1" \n\  
shift \n\  
echo "Started waiting for $@" \n\  
while pgrep -u "$USER" "$@" > /dev/null; do \n\  
echo "waiting ..." \n\  
sleep 1; \n\  
done \n\  
echo "$@ completed"' >> /usr/local/bin/waitfor \  
&& chmod +x /usr/local/bin/waitfor \  
&& which waitfor  
  
# Wine will not install/start without installing software-properties-common  
RUN apt-get update --assume-yes \  
&& apt-get install --no-install-recommends --assume-yes software-properties-
common \  
&& add-apt-repository --yes ppa:ricotz/unstable \  
&& apt-get purge --assume-yes software-properties-common \  
&& dpkg --add-architecture i386  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
wine2.0 \  
cabextract \  
xvfb \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -o /usr/local/bin/winetricks
https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
\  
&& chmod +x /usr/local/bin/winetricks \  
&& which winetricks  
  
RUN groupadd --system xclient \  
&& useradd --create-home --system --gid xclient xclient  
  
USER xclient  
  
# WINE  
#ENV WINEDEBUG -all,err+all  
ENV HOME /home/xclient  
ENV WINEPREFIX /home/xclient/.wine  
ENV WINEARCH win64  
WORKDIR /home/xclient  
  
RUN wine wineboot --init \  
&& waitfor xclient wineserver \  
&& wine --version  
  
#Extra corefonts, dotnet40  
RUN xvfb-run -a winetricks --unattended vcrun2010 \  
&& waitfor xclient wineserver  

