FROM gentoo/stage3-amd64  
RUN mkdir -p /root/build; \  
mkdir /usr/portage; \  
emerge-webrsync; \  
eselect python set python2.7; \  
echo 'MAKEOPTS="-j4"' >> /etc/portage/make.conf; \  
emerge --autounmask-write dev-vcs/git \  
dev-python/numpy \  
dev-python/requests \  
app-portage/portage-utils; \  
yes | etc-update --automode -3; \  
emerge --autounmask-write dev-vcs/git \  
dev-python/numpy \  
dev-python/requests \  
app-portage/portage-utils; \  
easy_install satispy; \  
easy_install pycosat; \  
cd /usr/portage; \  
rm -rf `ls -1A | grep -vP '^profiles'`;  
COPY scripts/ControlContainer/*.py scripts/ControlContainer/*.sh /root/  
COPY etc_portage /etc/portage/  
CMD ["/root/logger.sh"]  
  
  
# vim: ft=dockerfile :  

