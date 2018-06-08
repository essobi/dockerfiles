# SABnzbd  
#  
# Version: 0.0.13  
FROM fedora:24  
MAINTAINER Nicholas Moore  
  
VOLUME /config  
VOLUME /media  
ADD sabnzbd.sh /sabnzbd.sh  
  
RUN rpm -Uvh https://dl.dropboxusercontent.com/u/14500830/SABnzbd/16/SABnzbd-
release-1-3.noarch.rpm;\  
dnf -y install --nogpgcheck
http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E
%fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-
nonfree-release-$(rpm -E %fedora).noarch.rpm;\  
cp /usr/share/zoneinfo/US/Pacific /etc/localtime;\  
dnf -y install SABnzbd ;\  
groupadd -r -g 1000 sabnzbd ;\  
useradd -r -u 1000 -g 1000 sabnzbd ;\  
dnf clean all  
  
EXPOSE 8080  
ENTRYPOINT ["./sabnzbd.sh"]  

