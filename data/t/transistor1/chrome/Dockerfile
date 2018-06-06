#  
# Forked from Chrome Dockerfile  
#  
# https://github.com/dockerfile/chrome  
#  
# Pull base image.  
FROM debian:testing  
  
#These are placeholders for env vars  
ENV CHROMIUMUSER_USERNAME chromiumuser  
ENV CHROMIUMUSER_UID -  
ENV CHROMIUMUSER_GID -  
  
# Install Chromium.  
RUN apt-get update && \  
apt-get install -y wget dbus dbus-x11 && \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
apt-get update && apt-get install -y --force-yes google-chrome-stable
pulseaudio alsa-base alsa-tools alsa-utils sudo && \  
rm -rf /var/lib/apt/lists/*  
  
# Add the run-chrome script  
ADD run-chrome.sh /  
  
# Add the start script so that user doesn't need to download separately.  
ADD start.sh /  
  
# Add script to pull start.sh  
ADD config /bin/config  
  
# Define default command.  
CMD ["/run-chrome.sh"]  
  

