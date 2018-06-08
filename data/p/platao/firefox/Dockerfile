# Run container in Desktop:  
# xhost +local:docker;  
# docker run --rm --name firefox \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY \  
# -v ~/Desktop:/home \  
# -v /dev/shm:/dev/shm \  
# platao/firefox;  
# xhost -local:docker;  
FROM debian:sid  
  
RUN apt-get update && apt-get install -y \  
dirmngr \  
gnupg \  
\--no-install-recommends \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
0AB215679C571D1C8325275B9BDB3D89CE49EC21 \  
&& echo "deb http://ppa.launchpad.net/mozillateam/firefox-next/ubuntu xenial
main" >> /etc/apt/sources.list.d/firefox.list \  
&& apt-get update && apt-get install -y \  
ca-certificates \  
firefox \  
hicolor-icon-theme \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG en-US  
COPY local.conf /etc/fonts/local.conf  
VOLUME /home  
WORKDIR /home  
  
ENTRYPOINT ["/usr/bin/firefox"]  

