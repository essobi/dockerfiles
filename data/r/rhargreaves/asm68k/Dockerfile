FROM debian:stretch  
RUN dpkg --add-architecture i386 && \  
apt-get -y update && \  
apt-get -y install --no-install-recommends wine wine32 && \  
apt-get -y clean  
COPY asm68k.exe /app/  
ENV WINEDEBUG -all  
RUN bash -c 'wine Z:\\\app\\\asm68k.exe>/dev/null' || true  
  
VOLUME ["/src"]  
WORKDIR /src  
ENTRYPOINT ["wine", "Z:\\\app\\\asm68k.exe"]  
CMD [""]  

