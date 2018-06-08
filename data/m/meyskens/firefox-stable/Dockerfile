FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
firefox \  
hicolor-icon-theme \  
libasound2 \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
pulseaudio \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG en-US  
  
COPY local.conf /etc/fonts/local.conf  
  
RUN apt-get update && apt-get install -y ttf-mscorefonts-installer  
  
ENTRYPOINT [ "/usr/bin/firefox" ]

