# MotionEye  
FROM ubuntu:17.10  
LABEL maintainer="malvarez00@icloud.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV MOTIONEYE_VERSION="0.39"  
# Install motion, ffmpeg, v4l-utils and the dependencies from the repositories  
RUN apt-get update && \  
apt-get -y -f install \  
motion \  
ffmpeg \  
v4l-utils \  
python-pip \  
python-dev \  
curl \  
libssl-dev \  
libcurl4-openssl-dev \  
libjpeg-dev &&\  
apt-get clean  
  
# Install motioneye, which will automatically pull Python dependencies
(tornado, jinja2, pillow and pycurl)  
RUN pip install motioneye==$MOTIONEYE_VERSION  
  
# Prepare the configuration directory and the media directory  
RUN mkdir -p /etc/motioneye \  
mkdir -p /var/lib/motioneye  
  
# Configurations, Video & Images  
VOLUME ["/etc/motioneye", "/var/lib/motioneye"]  
  
# Start the MotionEye Server  
CMD test -e /etc/motioneye/motioneye.conf || \  
cp /usr/local/share/motioneye/extra/motioneye.conf.sample
/etc/motioneye/motioneye.conf ; \  
/usr/local/bin/meyectl startserver -c /etc/motioneye/motioneye.conf  
  
EXPOSE 8765  

