FROM alpine:edge  
  
MAINTAINER Michael Parker, <parkervcp+docker@gmail.com>  
  
RUN echo "http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk update && apk add mono git  
  
RUN mkdir /srv && git clone https://github.com/DeathCradle/Terraria-s-
Dedicated-Server-Mod.git /srv/tdsm  
  
WORKDIR /srv/tdsm/Binaries  
  
CMD ["mono", "TerrariaServer.exe", "-config", "server.config"]

