# Base docker image  
FROM sierratecnologia/java:7  
MAINTAINER Ricardo Rebello Sierra <contato@ricardosierra.com.br>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
wget \  
make \  
tar \  
libasound2 \  
libgconf-2-4 \  
libgnome-keyring-dev \  
libgtk2.0-0 \  
libnotify4 \  
libnss3 \  
libxtst6 \  
unzip \  
xz-utils \  
autoconf \  
file \  
g++ \  
gcc \  
make \  
pkg-config \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV SCILAB_VERSION 5.5.2  
RUN wget -c
http://www.scilab.org/download/${SCILAB_VERSION}/scilab-${SCILAB_VERSION}.bin.linux-i686.tar.gz
\  
&& tar -zxvf scilab-${SCILAB_VERSION}.bin.linux-i686.tar.gz \  
&& cd scilab-${SCILAB_VERSION} \  
&& cat README_Unix \  
&& ./bin/scilab  
  
# Autorun maltego  
ENTRYPOINT [ "scilab", "--foreground" ]  

