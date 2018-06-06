FROM debian:jessie  
  
RUN echo 'deb http://httpredir.debian.org/debian jessie main' >>
/etc/apt/sources.list && \  
apt-get update && apt-get install -y \  
chromium \  
chromium-l10n \  
fonts-liberation \  
fonts-roboto \  
hicolor-icon-theme \  
libcanberra-gtk-module \  
libexif-dev \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libpango1.0-0 \  
libv4l-0 \  
alsa-base \  
alsa-utils \  
pulseaudio \  
fonts-dejavu \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd -d /home/chromium -m -u 1000 -G audio chromium  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 740 /entrypoint.sh  
RUN mkdir /data \  
&& chown chromium. /data  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

