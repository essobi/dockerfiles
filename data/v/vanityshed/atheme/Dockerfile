FROM ubuntu:16.04  
MAINTAINER Stevesbrain  
  
ARG CONFIGUREFLAGS="--prefix=/services --disable-nls"  
ENV ATHEME_RELEASE 7.2.9  
# Build Atheme  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential curl
libssl-dev libssl1.0.0 openssl pkg-config git \  
&& mkdir /services \  
&& useradd -u 1000 -d /services atheme \  
&& mkdir /atheme-src && cd /atheme-src \  
&& curl -fsSL
"https://github.com/atheme/atheme/releases/download/v${ATHEME_RELEASE}/atheme-${ATHEME_RELEASE}.tar.bz2"
-o atheme.tar.bz2 \  
&& tar -jxf atheme.tar.bz2 --strip-components=1 \  
&& ./configure ${CONFIGUREFLAGS} \  
&& make \  
&& make install \  
&& apt-get purge -y build-essential git curl \  
#&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd /root \  
&& rm -rf /atheme-src \  
&& rm -rf /src; exit 0  
  
#Change ownership as needed  
RUN chown -R atheme:atheme /services  
#The user that we enter the container as, and that everything runs as  
USER atheme  
ENV BUILD 0.2.0  
ENTRYPOINT ["/services/bin/atheme-services", "-p", "/services/atheme.pid",
"-n"]  

