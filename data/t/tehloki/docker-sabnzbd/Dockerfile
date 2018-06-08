FROM fedora:26  
MAINTAINER Christopher Williams  
  
#  
# Add SABnzbd init script.  
#  
ADD sabnzbd.sh /sabnzbd.sh  
RUN chmod 755 /sabnzbd.sh  
  
#  
# Fix locales to handle UTF-8 characters.  
#  
ENV LANG C.UTF-8  
#  
# Install SABnzbd and all required dependencies.  
#  
RUN dnf -y install git \  
&& dnf -y install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-
nonfree-release-$(rpm -E %fedora).noarch.rpm \  
&& rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$(rpm -E
%fedora) \  
&& dnf -y install par2cmdline python-yenc python-cheetah unrar p7zip unzip
python-cryptography python-pip \  
&& dnf -y update \  
&& dnf clean all \  
&& rm -rf /var/cache/yum \  
&& pip install --upgrade pip \  
&& pip install sabyenc==3.3.1 \  
&& git clone https://github.com/sabnzbd/sabnzbd /opt/sabnzbd \  
&& cd /opt/sabnzbd \  
&& git checkout master  
  
#  
# Define container settings.  
#  
VOLUME ["/datadir", "/media"]  
  
EXPOSE 8080  
#  
# Start SABnzbd.  
#  
WORKDIR /opt/sabnzbd  
  
ENTRYPOINT ["/sabnzbd.sh"]  

