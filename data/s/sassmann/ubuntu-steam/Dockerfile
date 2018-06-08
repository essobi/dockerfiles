FROM ubuntu:16.04  
RUN echo 'deb [arch=amd64,i386 trusted=yes] http://repo.steampowered.com/steam
precise steam' > /etc/apt/sources.list.d/steam-inst.list && dpkg --add-
architecture i386  
RUN apt-get update \  
&& apt-get install -yq --no-install-recommends sudo libgl1-mesa-dri steam-
launcher pulseaudio ca-certificates \  
&& rm -rf /etc/apt/sources.list.d/steam-inst.list \  
&& apt-get update \  
&& apt-get install -yq libgl1-mesa-dri:i386 libgl1-mesa-glx:i386 libc6:i386
libnss3:i386 dbus:i386 dbus-x11:i386 \  
&& apt-get clean  
  
RUN echo 'steam ALL = NOPASSWD: ALL' > /etc/sudoers.d/steam  
RUN chmod 0440 /etc/sudoers.d/steam  
RUN adduser --disabled-password steam --gecos "Steam"  
  
USER steam  
ENV HOME /home/steam  
ENV PULSE_SERVER unix:/tmp/pulse  
  
CMD sudo /etc/init.d/dbus start && steam  

