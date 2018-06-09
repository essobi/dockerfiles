# VERSION: 0.1  
# DESCRIPTION: VNC server in a container  
# AUTHOR: John Andersen <johnandersenpdx@gmail.com>  
# COMMENTS:  
# This file builds a container which can be accessed via vnc  
# with username=user password=user. Useful as a base image  
# for a container which wishes to run and monitor gui software  
# USAGE:  
# # Download VNC Dockerfile  
# wget http://raw.githubusercontent.com/  
#  
# # Build VNC image  
# docker build -t VNC .  
#  
# # Run VNC container  
# docker run -d -p 5901:5901 --name vnc-server VNC  
FROM debian:8  
MAINTAINER John Andersen  
  
COPY ./vncpassword /tmp/vncpassword  
COPY ./startvnc /bin/startvnc  
COPY ./xstartup /home/user/.vnc/xstartup  
COPY ./startup.sh /startup.sh  
  
RUN apt-get -y update && \  
apt-get -y install dwm tightvncserver suckless-tools && \  
apt-get clean && \  
rm -rf /var/cache/apt/* && \  
/usr/sbin/useradd -m user && \  
chown -R user:user /home/user && \  
echo "user:user" | chpasswd user && \  
su - user -c "cat /tmp/vncpassword | vncserver" && \  
rm -fv /tmp/vncpassword && \  
su - user -c "vncserver -kill :1" && \  
sed -i 's/system("$xstartup >> " . &quotedString($desktopLog) . " 2>&1
&");/system("$xstartup 2>\&1");/g' /usr/bin/vncserver  
  
CMD ["/startup.sh"]  

