FROM phusion/baseimage:0.9.16  
MAINTAINER smdion <me@seandion.com>  
  
# Set correct environment variables  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Install beets and dependecies  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty
universe multiverse" && \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates
universe multiverse" && \  
apt-get update -q && \  
apt-get -qy --force-yes dist-upgrade && \  
apt-get install -qy --force-yes python-dev python-pip mp3gain wget && \  
yes | pip install beets && \  
yes | pip install pyacoustid && \  
yes | pip install pylast && \  
yes | pip install flask && \  
mkdir -p /root/.config/beets && \  
ln -s /config/config.yaml /root/.config/beets/config.yaml  
ADD src/fpcalc /usr/bin/fpcalc  
ADD src/ffmpeg /usr/bin/ffmpeg  
ADD src/ffprobe /usr/bin/ffprobe  
ADD src/lame /usr/bin/lame  
  
VOLUME ["/config", "/opt/downloads/music", "/opt/tmp"]  
  
EXPOSE 8337  
# Add edge.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD edge.sh /etc/my_init.d/edge.sh  
RUN chmod +x /etc/my_init.d/edge.sh  
  
# Add firstrun.sh to execute during container startup  
ADD firstrun.sh /etc/my_init.d/firstrun.sh  
RUN chmod +x /etc/my_init.d/firstrun.sh  
  
# Add web.sh to execute during container startup  
ADD web.sh /etc/my_init.d/web.sh  
RUN chmod +x /etc/my_init.d/web.sh  

