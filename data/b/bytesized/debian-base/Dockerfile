FROM debian:jessie  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && useradd -U -d /config -s
/bin/false bytesized  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN export DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive &&
\  
apt-get clean && apt-get update && \  
apt-get install -y -qq \  
locales && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
rm -rf /tmp/* /s6-overlay-amd64.tar.gz  
  
ENV LC_ALL="en_US.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"  
ADD /static /  
ENTRYPOINT ["/init"]  

