# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.17  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && apt-get install -y dictionaries-common  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty
universe multiverse" && apt-get update  
RUN apt-get install -y ubuntu-restricted-addons ubuntu-restricted-extras\  
alsa-utils alsa-tools alsa-base pavucontrol linux-sound-base\  
flashplugin-installer gstreamer1.0 gstreamer0.10-fluendo-mp3
gstreamer1.0-fluendo-mp3 gstreamer1.0-libav  
RUN apt-get update && apt-get install -fy rhythmbox  
  
RUN mkdir /etc/service/rhythmbox  
ADD run /etc/service/rhythmbox/run  
  
VOLUME /music  

