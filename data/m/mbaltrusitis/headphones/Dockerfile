FROM ubuntu:16.04  
MAINTAINER Matthew Baltrusitis <matthew@baltrusitis.com>  
  
ENV DEBIAN_FRONTEND="noninteractive"  
ENV HOME /opt/headphones  
  
RUN apt-get -qy update && \  
apt-get install -qy \  
ffmpeg \  
git \  
par2 \  
python-yenc \  
python-openssl \  
python-pip && \  
git clone https://github.com/rembo10/headphones.git $HOME && \  
touch /etc/default/headphones && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
VOLUME ["${HOME}"]  
EXPOSE 8181  
CMD ["python", "/opt/headphones/Headphones.py", "--host", "0.0.0.0"]  
  

