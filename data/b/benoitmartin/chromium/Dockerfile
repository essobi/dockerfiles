  
# check sound card index to use: cat /proc/asound/cards  
# cf: https://wiki.archlinux.org/index.php/Advanced_Linux_Sound_Architecture  
#run with:  
#docker run --rm -it --net host \  
# -e DISPLAY=unix$DISPLAY \  
# -e ALSA_CARD=0 \  
# -v ~/.Xauthority:/root/.Xauthority \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -v /var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket \  
# -v $HOME/.config/chromium/:/data \  
# -v $HOME/Downloads:/home/chromium/Downloads \  
# --device /dev/snd \  
# --device /dev/dri \  
# --name chromium \  
# benoitmartin/chromium  
FROM alpine:3.7  
LABEL maintainer "Benoit Martin <benoitmartin88@gmail.com>"  
  
RUN apk add --no-cache xorg-server mesa-dri-ati mesa-dri-intel ttf-freefont
chromium chromium-chromedriver  
  
# Add chromium user and set audio and video groups with correct gui  
RUN addgroup chromium && adduser -D -G chromium chromium \  
&& delgroup audio && addgroup -g 29 audio \  
&& delgroup video && addgroup -g 44 video \  
&& addgroup chromium audio && addgroup chromium video \  
&& mkdir -p /home/chromium/Downloads && chown -R chromium:chromium
/home/chromium  
  
# Run as non privileged user  
USER chromium  
  
ENTRYPOINT [ "chromium-browser" ]  
CMD [ "--no-sandbox", "--user-data-dir=/data" ]  
  

