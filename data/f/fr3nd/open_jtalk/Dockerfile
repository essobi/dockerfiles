FROM debian:jessie  
MAINTAINER Carles Amigó, fr3nd@fr3nd.net  
  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
lame \  
unzip \  
&& rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/info/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
WORKDIR /opt  
RUN curl -L http://downloads.sourceforge.net/hts-
engine/hts_engine_API-1.10.tar.gz | tar xvz  
WORKDIR /opt/hts_engine_API-1.10  
RUN ./configure --prefix=/usr && make && make install  
  
WORKDIR /opt  
RUN mkdir -p /usr/lib/hts-voice  
RUN curl -L http://downloads.sourceforge.net/open-
jtalk/hts_voice_nitech_jp_atr503_m001-1.05.tar.gz | tar xvz && \  
mv /opt/hts_voice_nitech_jp_atr503_m001-1.05/*.htsvoice /usr/lib/hts-voice/ &&
\  
rm -rf /opt/hts_voice_nitech_jp_atr503_m001-1.05  
RUN curl -L
http://sourceforge.net/projects/mmdagent/files/MMDAgent_Example/MMDAgent_Example-1.4/MMDAgent_Example-1.4.zip/download
> MMDAgent_Example.zip && \  
unzip -x MMDAgent_Example.zip && \  
rm -f MMDAgent_Example.zip && \  
mv /opt/MMDAgent_Example-1.4/Voice/mei/*.htsvoice /usr/lib/hts-voice/ && \  
rm -rf /opt/MMDAgent_Example-1.4  
  
  
WORKDIR /opt  
RUN curl -L http://downloads.sourceforge.net/open-jtalk/open_jtalk-1.09.tar.gz
|tar xvz  
WORKDIR /opt/open_jtalk-1.09  
RUN ./configure \  
\--with-charset=UTF-8 \  
\--prefix=/usr \  
\--with-hts-engine-header-path=/usr/include/ \  
\--with-hts-engine-library-path=/usr/lib/ && make && make install  
  
WORKDIR /  

