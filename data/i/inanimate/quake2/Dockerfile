FROM debian:jessie  
  
## The Data from the official point release.  
ENV quake2_data q2-3.20-x86-full-ctf.exe  
  
RUN echo "deb http://httpredir.debian.org/debian jessie contrib" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y quake2-server \  
wget && \  
apt-get clean  
  
RUN rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/locale/* \  
/var/cache/debconf/*-old \  
/var/lib/apt/lists/* \  
/usr/share/doc/*  
  
WORKDIR /usr/share/games/quake2  
  
RUN wget "http://youfailit.net/pub/idgames/idstuff/quake2/${quake2_data}" && \  
chmod +x ${quake2_data} && \  
unzip ${quake2_data} && \  
rm -rf ${quake2_data}  
  
USER quake2-server  
  
EXPOSE 27910/udp  
  
ENTRYPOINT ["/usr/games/quake2-server"]  
  
CMD ["+exec", "server.cfg", "+map", "q2dm1"]  

