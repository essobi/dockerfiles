FROM debian:stable-slim  
MAINTAINER LLC CERERIS <dev@cereris.org>  
  
RUN apt-get update && apt-get -y install \--no-install-recommends wget curl
xz-utils ca-certificates gcc libc6-dev && \  
wget https://dlang.org/install.sh \--no-check-certificate && \  
bash install.sh install -p /dlang dmd-2.075.0 && \  
rm install.sh && \  
apt-get -y purge wget xz-utils ca-certificates openssl libssl* libgssapi*
libldap* && \  
apt-get -y install curl \--no-install-recommends && \  
rm -rf /dlang/dmd-*/html && \  
rm -rf /dlang/dub*/dub.tar.gz && \  
rm -rf /dlang/README.TXT && \  
rm -rf /dlang/dmd*/README.TXT && \  
rm -rf /dlang/dmd*/activate* && \  
rm -rf /dlang/install.sh && \  
rm -rf /dlang/dmd*/freebsd && \  
rm -rf /dlang/dmd*/license.txt && \  
rm -rf /dlang/dmd*/osx && \  
rm -rf /dlang/dmd*/linux/lib32 && \  
rm -rf /dlang/dmd*/man && \  
rm -rf /dlang/dmd*/samples && \  
rm -rf /dlang/dmd*/solaris && \  
rm -rf /dlang/dmd*/windows && \  
rm -rf /dlang/dmd*/linux/bin32 && \  
apt-get -y autoremove && apt-get clean && apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* && rm -rf /usr/share/doc && rm -rf /usr/share/man
&& rm -rf /usr/share/locale  
  
ENV PATH=/dlang/dub:/dlang/dmd-2.075.0/linux/bin64:${PATH} \  
LD_LIBRARY_PATH=/dlang/dmd-2.075.0/linux/lib64 \  
LIBRARY_PATH=/dlang/dmd-2.075.0/linux/lib64 \  
PS1="(dmd-2.075.0) \\\u@\\\h:\\\w\$"  

