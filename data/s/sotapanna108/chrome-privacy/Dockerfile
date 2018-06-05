FROM ubuntu:16.04  
  
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf && \  
apt-get update && apt-get install -y \  
ca-certificates \  
curl \  
gnupg \  
pulseaudio \  
hicolor-icon-theme \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libexif-dev \  
libv4l-0 \  
fonts-symbola \  
\--no-install-recommends \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add
\- \  
&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google.list \  
&& apt-get update && apt-get install -y \  
google-chrome-stable \  
\--no-install-recommends \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
  
COPY local.conf /etc/fonts/local.conf  
ADD chrome-state /data  
  
RUN \  
useradd -ms /bin/bash chrome && \  
mkdir -p /home/chrome/parent_home && \  
chmod -R 777 /home/chrome/parent_home && \  
chown -R chrome. /data /home/chrome  
  
USER chrome  
  
ENTRYPOINT [ "google-chrome" ]  
CMD [ "--user-data-dir=/data", "--disable-sync", "--incognito" ]  

