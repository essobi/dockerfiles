FROM node:8.2.1  
MAINTAINER Christian Hoffmeister <mail@choffmeister.de>  
  
ENV DOCKER_VERSION="1.12.3"  
WORKDIR /tmp  
RUN echo 'deb http://ftp.uk.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list && \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
apt-get update && \  
apt-get install -y xvfb matchbox-window-manager ffmpeg google-chrome-stable &&
\  
apt-get clean  
RUN \  
wget https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz &&
\  
echo "a3bb88649bcc47775c29dab7d95709f4dda04d0e docker-$DOCKER_VERSION.tgz" |
shasum -c - && \  
tar xf docker-$DOCKER_VERSION.tgz && \  
mv docker /opt/docker && \  
ln -s /opt/docker/docker /usr/bin/docker && \  
rm -r docker-$DOCKER_VERSION.tgz  
  
ENV DISPLAY_WIDTH 1280  
ENV DISPLAY_HEIGHT 720  
COPY xvfb-run-record /usr/bin/xvfb-run-record  
RUN chmod +x /usr/bin/xvfb-run-record  
COPY xvfb-run-simple /usr/bin/xvfb-run-simple  
RUN chmod +x /usr/bin/xvfb-run-simple  
  
WORKDIR /root  

