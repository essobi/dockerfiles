FROM debian:jessie-slim  
  
# INSTALLATION  
RUN echo "deb http://ftp.fr.debian.org/debian jessie main contrib non-free" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get -y install python python-scapy python-feedparser python-cherrypy3 \  
nmap hping3 nikto tcpreplay apache2-utils \  
build-essential checkinstall libssl-dev libssh-dev \  
wget python-paramiko sudo tcpdump  
  
# NCRACK  
ENV NCRACK_VERSION 0.5  
RUN wget https://nmap.org/ncrack/dist/ncrack-$NCRACK_VERSION.tar.gz \  
&& tar -xzf ncrack-$NCRACK_VERSION.tar.gz \  
&& cd ncrack-$NCRACK_VERSION \  
&& ./configure \  
&& make \  
&& make install  
  
# PYTBULL  
ENV PYTBULL_VERSION 2.1  
RUN wget
https://downloads.sourceforge.net/project/pytbull/pytbull-$PYTBULL_VERSION.tar.bz2
\  
&& bzip2 -cd pytbull-$PYTBULL_VERSION.tar.bz2 | tar xf - \  
&& mv pytbull/ /opt/ \  
&& cd /opt/pytbull  
COPY config.cfg.tpl /opt/pytbull/conf/config.cfg.tpl  
  
## CONFIGURATION  
RUN sed -i 's/\/data\/tools\/nikto-2.1.5\/nikto.pl/\/usr\/bin\/nikto/'
/opt/pytbull/conf/config.cfg \  
&& sed -i 's/\/data\/tools\/nikto-2.1.5\/nikto.conf/\/etc\/nikto\/config.txt/'
/opt/pytbull/conf/config.cfg  
  
# CLEAN  
RUN apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
ADD entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh  
  
WORKDIR /opt/pytbull  
  
ENTRYPOINT ["/entrypoint.sh"]  

