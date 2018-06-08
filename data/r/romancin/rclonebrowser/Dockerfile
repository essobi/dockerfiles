## Custom Dockerfile  
FROM consol/ubuntu-xfce-vnc:latest  
MAINTAINER Romancin "roman.martin84@gmail.com"  
ENV REFRESHED_AT 2018-03-04  
  
## Install Rclone  
USER 0  
  
RUN apt-get update && \  
apt-get -y install curl unzip software-properties-common python-software-
properties && \  
curl -O https://downloads.rclone.org/rclone-current-linux-amd64.zip && \  
unzip rclone-current-linux-amd64.zip && \  
cd rclone-*-linux-amd64 && \  
cp rclone /usr/bin/ && \  
chown root:root /usr/bin/rclone && \  
chmod 755 /usr/bin/rclone && \  
mkdir -p /usr/local/share/man/man1 && \  
cp rclone.1 /usr/local/share/man/man1/ && \  
mandb && \  
add-apt-repository ppa:mmozeiko/rclone-browser && \  
apt-get update && \  
apt-get install -y rclone-browser && \  
ln -s /usr/bin/rclone-browser /headless/Desktop/rclone-browser  
  
## switch back to default user  
USER 1984  
  
VOLUME /config  

