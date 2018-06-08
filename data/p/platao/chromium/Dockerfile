# Run container in Desktop:  
# xhost +local:docker;  
# docker run --rm --name chromium \  
# --cap-add=SYS_ADMIN \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -v /dev/shm:/dev/shm \  
# -e DISPLAY \  
# platao/chromium;  
# xhost -local:docker;  
FROM alpine  
  
ENV VERSION 0.0.1  
# Optional Configuration Parameter  
ARG SERVICE_USER  
ARG SERVICE_HOME  
  
# Default Settings  
ENV SERVICE_USER ${SERVICE_USER:-chromium}  
ENV SERVICE_HOME ${SERVICE_HOME:-/home/${SERVICE_USER}}  
  
  
RUN adduser -h ${SERVICE_HOME} -s /sbin/nologin -u 1000 -D ${SERVICE_USER} &&
\  
apk add --no-cache \  
chromium \  
dumb-init \  
dbus-x11 \  
udev \  
mesa-gl \  
mesa-dri-swrast \  
ttf-freefont  
  
USER ${SERVICE_USER}  
WORKDIR ${SERVICE_HOME}  
VOLUME ${SERVICE_HOME}  
  
ENTRYPOINT ["/usr/bin/dumb-init", "/usr/bin/chromium-browser"]  

