FROM buildpack-deps:xenial  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
devscripts \  
cdbs \  
gengetopt \  
libjson0-dev \  
quilt \  
debhelper \  
dh-buildinfo \  
config-package-dev php7.0-cli \  
nodejs npm nodejs-legacy \  
lsb-release \  
composer \  
&& rm -rf /var/lib/apt/lists/*  
RUN npm install -g bower  
  
RUN dpkg --add-architecture armhf; dpkg --add-architecture i386  
RUN sed -i 's/deb http/deb [arch=amd64,i386] http/' /etc/apt/sources.list  
RUN echo 'deb [arch=armhf] http://ports.ubuntu.com/ xenial main universe
restricted' >> /etc/apt/sources.list  
RUN echo 'deb [arch=armhf] http://ports.ubuntu.com/ xenial-updates main
universe restricted' >> /etc/apt/sources.list  
RUN ln -s /usr/bin/strip /usr/bin/i686-linux-gnu-strip  
  
RUN apt-get update  
RUN apt-get -y install crossbuild-essential-armhf \  
crossbuild-essential-armel git debhelper libc6-dev gengetopt libtool automake
\  
libssl-dev libjson0-dev libssl-dev:armhf libjson0-dev:armhf \  
libssl-dev:i386 libjson0-dev:i386 \  
&& rm -rf /var/lib/apt/lists/*  

