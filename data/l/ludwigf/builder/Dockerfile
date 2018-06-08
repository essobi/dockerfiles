FROM fedora:25  
  
COPY requirements.txt package.json /root/  
  
RUN \  
# enable rpm fusion \  
dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-
release-$(rpm -E %fedora).noarch.rpm
https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm
-E %fedora).noarch.rpm && \  
dnf install -y python-pip gcc gcc-c++ make nodejs npm bzip2 nodejs npm git \  
libffi-devel redhat-rpm-config python-devel ffmpeg-devel \  
libxml2-devel libxslt-devel xorg-x11-server-Xvfb \  
xorg-x11-xauth which docker && \  
cd /root && \  
pip install -r /root/requirements.txt && \  
npm install -g && \  
dnf clean all && \  
rm -rf /tmp/*  
  
WORKDIR /app  

