FROM ubuntu:14.04  
MAINTAINER frostasm  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q -y update && apt-get -q -y dist-upgrade && apt-get install -q
-y \--no-install-recommends \  
gstreamer1.0-plugins-base \  
gstreamer1.0-plugins-good \  
gstreamer1.0-plugins-bad \  
gstreamer1.0-plugins-ugly \  
gstreamer1.0-libav  
  
  
RUN apt-get install -q -y wget \  
&& wget http://deb.openalpr.com/openalpr.gpg.key -O /tmp/openalpr.gpg.key \  
&& apt-key add /tmp/openalpr.gpg.key \  
&& echo "deb http://deb.openalpr.com/master/ openalpr main" >
/etc/apt/sources.list.d/openalpr.list \  
&& apt-get -q -y update && apt-get -q -y dist-upgrade && apt-get install -q -y
\  
libcv2.4 \  
libtesseract3 \  
beanstalkd \  
openalpr \  
openalpr-daemon  
  
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
  
# Add group & user  
#RUN groupadd -r user && useradd \--create-home --gid user user && echo 'user
ALL=NOPASSWD: ALL' > /etc/sudoers.d/user  
  
#USER user  
#WORKDIR /home/user  

