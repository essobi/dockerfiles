FROM phusion/baseimage:0.9.18  
MAINTAINER Benni-chan  
  
# Set correct environment variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV TERM xterm  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
wget \  
python \  
xdg-utils \  
ImageMagick && \  
mkdir /opt/calibre  
  
RUN mkdir /config  
  
VOLUME ["/config"]  
  
EXPOSE 8080  
RUN cd /opt && \  
wget --no-check-certificate -nv -O-
https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-
installer.py | python -c "import sys; main=lambda:sys.stderr.write('Download
failed\n'); exec(sys.stdin.read()); main('/opt/', True)"  
  
# Add firstrun.sh to execute during container startup  
ADD firstrun.sh /etc/my_init.d/firstrun.sh  
RUN chmod +x /etc/my_init.d/firstrun.sh  

