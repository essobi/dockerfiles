FROM alpine  
LABEL maintainer="Nicolas Guillaumin <nicolas+docker@guillaumin.me>"  
  
RUN apk add --no-cache build-base  
RUN wget -q http://server.owl.de/~frank/tags/vasm1_8a.tar.gz  
RUN tar xzvf vasm1_8a.tar.gz  
  
WORKDIR vasm  
RUN for CPU in 6502 6800 arm c16x jagrisc m68k ppc test tr3200 vidcore x86
z80; do\  
for SYNTAX in std madmac mot oldstyle; do\  
make CPU=${CPU} SYNTAX=${SYNTAX};\  
done;\  
done  
RUN install vasm*_* /usr/local/bin  
  
WORKDIR /  
RUN rm -Rf vasm*.tar.gz vasm/  

