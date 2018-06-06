FROM alpine:latest  
LABEL original.github "https://github.com/mrorgues/dockerfiles"  
  
# docker run --rm -it \  
# --net host \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# --device /dev/snd \  
# -v /dev/shm:/dev/shm \  
# -v /etc/fonts:/etc/fonts \  
# -v /usr/share/fonts:/usr/share/fonts \  
# -v $HOME/.mozilla:/root/.mozilla \  
# --ipc="host" \  
# --name firefox-esr \  
# icloak/firefox-esr  
RUN apk add --no-cache \  
ca-certificates \  
firefox-esr \  
dbus \  
libcanberra-gtk2 && \  
rm -rf /tmp/*  
  
RUN addgroup -g 1003 volatile && \  
adduser -D -h /home/ICLOAK -u 1001 volatile -G volatile  
  
USER volatile  
  
CMD [ "/usr/bin/firefox" ]

