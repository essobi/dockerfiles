FROM frolvlad/alpine-glibc:alpine-3.4  
MAINTAINER Jarrod Pas <jarrodpas@gmail.com>  
  
RUN apk --no-cache add tini  
ENTRYPOINT ["/sbin/tini", "--"]  
  
ENV VERSION=0.15.40  
RUN apk --no-cache add curl \  
&& curl -sSLo /tmp/factorio.tar https://www.factorio.com/get-
download/${VERSION}/headless/linux64 \  
&& mkdir -p /opt \  
&& tar xf /tmp/factorio.tar -C /opt \  
&& rm /tmp/factorio.tar \  
&& apk --no-cache del curl  
  
ADD rootfs /  
  
VOLUME /saves  
VOLUME /scenarios  
VOLUME /mods  
  
EXPOSE 34197/udp  
EXPOSE 27015/udp  
  
ENV FACTORIO_SAVE=server.zip \  
FACTORIO_RCON_PASSWORD=  
  
CMD ["/cmd.sh"]  
  

