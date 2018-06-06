  
FROM opensuse:13.2  
# Command to add needed repos:  
RUN zypper ar -f http://download.opensuse.org/update/13.2/ update && \  
zypper ar -f http://ftp.gwdg.de/pub/linux/packman/suse/openSUSE_13.2/ packman
&& \  
zypper ar -f
http://download.opensuse.org/repositories/Education/openSUSE_13.2/ education
&& \  
zypper ar -f
http://download.opensuse.org/repositories/devel:/languages:/python/openSUSE_13.2/
obsPython  
  
# Add rtadmin and meduser/sdc users:  
RUN useradd -d /home/rtadmin -m -u 999 -g 100 -G users,audio -s /bin/bash
rtadmin  
  
RUN useradd -d /home/meduser -m -u 1000 -g 100 -G users,audio -s /bin/bash
meduser  
  
# To install AFNI libraries:  
# krb5-mini conflicts with samba installation  
RUN zypper --gpg-auto-import-keys --non-interactive remove krb5-mini  
  
RUN zypper --gpg-auto-import-keys --non-interactive install \  
libxft-devel libxp-devel libxpm-devel \  
libxmu-devel libpng12-devel libjpeg62 \  
zlib-devel libxt-devel libxext-devel \  
libexpat-devel netpbm libnetpbm-devel \  
libGLU1 tcsh vim tar which less \  
python-numpy python-matplotlib python-dicom \  
dcmtk libdcmtk3_6 kradview samba ntp \  
wget cmake gcc gcc-c++ xeyes  
  
ADD ntp.conf /etc  
# ADD smb.conf /etc/samba  
ADD meduser.bashrc /home/meduser/.bashrc  
ADD .afnirc /home/rtadmin  
ADD rtadmin.bashrc /home/rtadmin/.bashrc  
RUN mkdir -p /home/rtadmin/RTafni/src /home/rtadmin/RTafni/bin/AFNI
/home/rtadmin/RTafni/var/log/RTafni.log
/home/rtadmin/RTafni/var/spool/cron/tabs /home/rtadmin/RTafni/tmp  
ADD RTafni checkAndKeepAlive.sh dcmListenerRT.py utilsDICOM.py
@update.afni.binaries /home/rtadmin/RTafni/bin/  
ADD getBuildInstallGDCM.sh /home/rtadmin/RTafni/src  
  
# To determine if these are left in default Dockerfile, as they lead to  
# the final image being ~ 6.5 GB, or left for the user to download a  
# smaller image, and run these the first time the container is launched.  
RUN /home/rtadmin/RTafni/bin/\@update.afni.binaries -package linux_openmp_64
-bindir /home/rtadmin/RTafni/bin/AFNI/  
RUN cd /home/rtadmin/RTafni/src && ./getBuildInstallGDCM.sh  
  
RUN chown -R rtadmin:users /home/rtadmin  
# RUN chown -R meduser:users /home/rtadmin/RTafni/var/log
/home/rtadmin/RTafni/tmp  
ADD .startup /root  
  
# Allow Siemens console access to the Samba shares and start it monitoring for
RT  
# RUN smbpasswd -L -n -a meduser  
# Location for volume from host to be mounted in container  
VOLUME ["/data0"]  
  
# Ports on container to be exposed/passed through to host  
# # nmbd smbd smbd smbd Port chosen for Siemens RT  
# EXPOSE 138:138/udp 139:139 445:445 445:445/udp 8111:8111  
# Start up Samba services using default command to run at container startup  
ENTRYPOINT ["/bin/bash", "/root/.startup"]  
  

