############################################################  
# Dockerfile for SSH with high performance patch.  
#  
# Based on Arch Linux  
############################################################  
  
FROM yantis/archlinux-small  
MAINTAINER Jonathan Yantis <yantis@yantis.net>  
  
ADD keyfix/keyfix.sh /usr/bin/keyfix  
ADD openssh /service/openssh  
  
# No longer update  
RUN pacman -Syy --noconfirm && \  
  
# Install open ssh  
# RUN pacman --noconfirm -S openssh  
# Install SSH with the high performance patch.  
# REM this section to not use the high performance patch  
#### - SSH-HP START #########  
pacman --noconfirm -S yaourt gcc make git autoconf fakeroot binutils && \  
runuser -l docker -c "yaourt --noconfirm -S openssh-hpn-git" && \  
pacman --noconfirm -Rs yaourt gcc make git autoconf fakeroot binutils && \  
  
# Allow clients to use the NONE cipher  
# http://www.psc.edu/index.php/hpn-ssh/640  
echo "NoneEnabled=yes" >> /etc/ssh/sshd_config && \  
# pacman --noconfirm -Rs linux-headers openbsd-netcat && \  
#### - SSH-HP END #########  
# Setup our SSH  
echo "PasswordAuthentication no" >> /etc/ssh/sshd_config && \  
  
# Disable PAM so the container doesn't need privs.  
sed -i "s/UsePAM yes/UsePAM no/" /etc/ssh/sshd_config && \  
  
# Some people have more than 6 keys in memory. Lets allow up to 30 tries.  
echo "MaxAuthTries 30" >> /etc/ssh/sshd_config && \  
  
touch /var/log/lastlog && \  
chgrp utmp /var/log/lastlog && \  
chmod 664 /var/log/lastlog && \  
  
mkdir -p $HOME/.ssh && \  
  
# Add in an.ssh directory for our user.  
mkdir -p /home/docker/.ssh && \  
chown docker:users /home/docker/.ssh && \  
  
##########################################################################  
# CLEAN UP SECTION - THIS GOES AT THE END #  
##########################################################################  
# Remove anything left in temp.  
rm -r /tmp/* && \  
  
bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \  
paccache -rk0 >/dev/null 2>&1 && \  
pacman-optimize && \  
rm -r /var/lib/pacman/sync/* && \  
  
# Dynamically accept either passed in keys OR password but not both.  
# And make it so it doesn't matter what UID the authorized_keys volume is.  
chmod +x /usr/bin/keyfix  
  
CMD ["/init"]  

