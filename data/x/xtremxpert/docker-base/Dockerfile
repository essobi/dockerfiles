FROM debian:jessie  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xvzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
LANG="fr_CA.UTF-8" \  
LC_ALL="fr_CA.UTF-8" \  
LANGUAGE="fr_CA.UTF-8" \  
TZ="America/Toronto" \  
TERM="xterm"  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install ---no-install-recommends --no-install-suggests -yqq \  
locales \  
mc \  
nano \  
tzdata \  
&& \  
echo $TZ > /etc/timezone && \  
dpkg-reconfigure tzdata && \  
echo 'alias ll="ls -lah --color=auto"' >> /etc/bash.bashrc && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
echo "fr_CA.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen fr_CA.UTF-8 && \  
dpkg-reconfigure locales && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
echo 'alias ll="ls -lah --color=auto"' >> /etc/bash.bashrc  
  
ENTRYPOINT ["/init"]  

