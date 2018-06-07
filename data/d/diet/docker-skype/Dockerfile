# Base docker image based on work of Daniel Mizyrycki <daniel@docker.com>  
FROM debian:wheezy  
  
# Setup multiarch because Skype is 32bit only  
RUN dpkg --add-architecture i386  
  
# Install Iceweasel and "sudo"  
RUN apt-get update && apt-get install -y sudo  
  
# Install PulseAudio for i386 (64bit version does not work with Skype)  
RUN apt-get install -y libpulse0:i386 pulseaudio:i386  
  
# create skype user  
RUN \  
adduser --disabled-password --gecos '' skype \  
&& adduser skype sudo \  
&& echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# Install Skype  
RUN apt-get install -y wget  
RUN wget http://download.skype.com/linux/skype-debian_4.3.0.37-1_i386.deb -O
/usr/src/skype.deb  
RUN dpkg -i /usr/src/skype.deb || true  
RUN apt-get update  
RUN apt-get install -fy # Automatically detect and install dependencies  
  
# Enable camera  
RUN apt-get install -y libv4l-0:i386  
  
ENV QT_X11_NO_MITSHM 1  
ENV GNOME_DESKTOP_SESSION_ID this-is-deprecated  
ENV PULSE_SERVER /data/.pulse/.socket  
  
ADD bin/skype.run /app/host/skype.run  
ADD bin/skype /app/skype  
  
USER skype  
CMD "/app/skype"  

