FROM debian:jessie  
  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
m4 \  
ca-certificates \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -o /root/bison-3.0.4.tar.xz -fSL
http://www.nic.funet.fi/pub/gnu/ftp.gnu.org/pub/gnu/bison/bison-3.0.4.tar.xz \  
&& curl -o /root/bison-3.0.4.tar.xz.sig -L
http://www.nic.funet.fi/pub/gnu/ftp.gnu.org/pub/gnu/bison/bison-3.0.4.tar.xz.sig
\  
&& curl -o /root/flex-latest.tar.gz -fSL
https://github.com/westes/flex/archive/master.zip \  
# && curl -o /root/flex-2.6.3.tar.gz -fSL
https://github.com/westes/flex/releases/download/v2.6.3/flex-2.6.3.tar.gz \  
&& gpg --keyserver keys.gnupg.net --recv-keys 78D5264E \  
&& gpg --verify /root/bison-3.0.4.tar.xz.sig \  
&& cd /root/ \  
&& tar -xf bison-3.0.4.tar.xz \  
&& cd bison-3.0.4 \  
&& ./configure --disable-dependency-tracking \  
&& make \  
&& make install \  
&& cd /root/ \  
&& tar -xf flex-latest.tar.gz \  
&& cd flex-latest \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /root/flex-2.6.3.tar.gz \  
/root/bison-3.0.4.tar.xz.sig \  
/root/bison-3.0.4.tar.xz \  
/root/bison-3.0.4 \  
/root/flex-2.6.3  

