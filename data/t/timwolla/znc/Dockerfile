FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y libssl1.0.0 libicu52 --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /home/znc  
  
RUN groupadd -r znc \  
&& useradd -r -g znc znc \  
&& chown znc:znc /home/znc  
  
ENV ZNC_VERSION 1.6.5  
RUN buildDeps='libssl-dev libicu-dev g++ make curl pkg-config' \  
&& apt-get update && apt-get install -y ca-certificates $buildDeps \--no-
install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -fsSL http://znc.in/releases/archive/znc-$ZNC_VERSION.tar.gz -o
znc.tar.gz \  
&& mkdir -p /usr/local/src/znc \  
&& tar xvf "znc.tar.gz" -C /usr/local/src/znc --strip-components=1 \  
&& rm "znc.tar.gz" \  
&& cd /usr/local/src/znc \  
&& ./configure \  
&& cd / \  
&& make -C /usr/local/src/znc \  
&& make -C /usr/local/src/znc install \  
&& rm -rf /usr/local/src/znc \  
&& apt-get purge -y --auto-remove $buildDeps  
  
USER znc  
  
CMD [ "znc", "-f" ]  

