FROM gocd/gocd-agent  
  
MAINTAINER Abdulkadir Yaman <abdulkadiryaman@gmail.com>  
  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
ca-certificates \  
fonts-takao \  
gconf-service \  
gksu \  
libappindicator1 \  
libasound2 \  
libcurl3 \  
libgconf-2-4 \  
libnspr4 \  
libnss3 \  
libxss1 \  
libpango1.0-0 \  
pulseaudio \  
python-psutil \  
supervisor \  
wget \  
xbase-clients \  
xdg-utils \  
xvfb \  
firefox  
  
RUN rm -rf /var/lib/apt/lists/*  
  
ADD https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
/chrome.deb  
  
RUN dpkg -i /chrome.deb && rm /chrome.deb  
  
RUN ln -s /lib/x86_64-linux-gnu/libudev.so.1 /lib/x86_64-linux-
gnu/libudev.so.0  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
VOLUME ["/home/chrome"]  
  
RUN useradd -m -G pulse-access chrome  
  
ADD autoregister.properties /var/lib/go-agent/config/autoregister.properties  
  
RUN ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

