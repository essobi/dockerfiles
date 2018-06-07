FROM fedora  
MAINTAINER Andrey Yudin <rogue@roguelabs.tech>  
COPY . /root/discord-bot  
WORKDIR /root/discord-bot  
RUN su -c 'dnf install http://download1.rpmfusion.org/free/fedora/rpmfusion-
free-release-$(rpm -E %fedora).noarch.rpm
http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm
-E %fedora).noarch.rpm -y'  
RUN dnf install ffmpeg python3-devel gcc libffi-devel redhat-rpm-config make
libtool -y  
RUN pip3 install -r requirements.txt  
CMD python3 bot.py  

