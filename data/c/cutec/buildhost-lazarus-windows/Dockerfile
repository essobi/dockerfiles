FROM jedisct1/phusion-baseimage-latest  
MAINTAINER archedraft  
  
# Set correct environment variables  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN apt-get update && apt-get -y install xvfb \  
x11vnc \  
xdotool \  
wget \  
supervisor \  
x11-apps \  
wine-stable \  
net-tools  
RUN dpkg --add-architecture i386 && apt-get update && apt-get -y install
wine32  
RUN rm -rf /var/lib/apt/lists/*  
  
ENV DISPLAY :0.0  
WORKDIR /root/  
ADD novnc /root/novnc/  
ADD lazarus /root/.wine/  
COPY startup.sh /usr/local/bin/startup.sh  
  
# Expose Port  
EXPOSE 8080  
ENV WINEPATH
"C:/lazarus;c:\lazarus\mingw\i386-win32\bin;c:/lazarus/fpc/2.6.4/bin/i386-win32;c:/Program
Files (x86)/Git/bin"  
ENTRYPOINT ["bash","/usr/local/bin/startup.sh"]  
CMD ["dir"]  

