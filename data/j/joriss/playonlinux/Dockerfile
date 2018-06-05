FROM ubuntu:14.04  
MAINTAINER Joris Schalk  
  
RUN dpkg --add-architecture i386  
RUN apt-get install -y software-properties-common && add-apt-repository -y
ppa:ubuntu-wine/ppa  
RUN apt-get update -y  
  
#Install Wine to get rid of a few notification in playonlinux  
RUN apt-get install -qy wine1.7 winetricks wget libcanberra-gtk-module gettext  
# gettext libgl1-mesa-dri:i386 libgl1-mesa-glx:i386 libfreetype6:i386
libcanberra-gtk-module  
#Install playonlinux (instructions on site)  
RUN wget -q "http://deb.playonlinux.com/public.gpg" -O- | sudo apt-key add -  
RUN wget http://deb.playonlinux.com/playonlinux_trusty.list -O
/etc/apt/sources.list.d/playonlinux.list  
RUN apt-get update -y  
RUN apt-get install -y playonlinux  
  
#Change encoding for correct language select screens in playonlinux  
RUN sed -i 's/encoding = \"ascii\"/encoding = \"utf-8\"/g'
/usr/lib/python2.7/site.py  
  
#Cleanup  
RUN apt-get autoremove &&\  
apt-get clean &&\  
rm -rf /tmp/*  
  
# Create a user to run as  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/gamer && \  
echo "gamer:x:${uid}:${gid}:gamer,,,:/home/gamer:/bin/bash" >> /etc/passwd &&
\  
echo "gamer:x:${uid}:" >> /etc/group && \  
echo "gamer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/gamer && \  
chmod 0440 /etc/sudoers.d/gamer && \  
chown ${uid}:${gid} -R /home/gamer &&\  
usermod -a -G video gamer  
  
#Use created user  
USER gamer  
ENV HOME /home/gamer  
ENV USER gamer  
  
CMD playonlinux  

