FROM debian:stretch  
MAINTAINER François Billant <fbillant@gmail.com>  
  
RUN useradd -ms /bin/bash ff  
  
ENV VERSION=60.0.1  
RUN sed -i.bak 's/stretch main/stretch main contrib non-free/g'
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y \  
pulseaudio \  
wget \  
bzip2 \  
libgtk-3-0 \  
libdbus-glib-1-2 \  
libxt6 \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /home/ff &&\  
wget --no-check-certificate
https://ftp.mozilla.org/pub/firefox/releases/$VERSION/linux-x86_64/en-
US/firefox-$VERSION.tar.bz2 && \  
tar -xvf firefox-$VERSION.tar.bz2 && \  
rm firefox-$VERSION.tar.bz2  
  
ENTRYPOINT ["/home/ff/firefox/firefox"]  

