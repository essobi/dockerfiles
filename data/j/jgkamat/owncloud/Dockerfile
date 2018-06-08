FROM ubuntu:14.04  
# This is a dockerfile that builds an owncloud service and sets it up as much
as possible!  
# to build: 'docker build -t jgkamat/owncloud .'  
# Lets see if we can use this instead later!  
#FROM phusion/baseimage:latest  
# The base image changes policy-rc.d to stop services from being configured by
apt. We change this to mirror stock Ubuntu.  
RUN rm /usr/sbin/policy-rc.d  
ADD setupScripts/init-fake.conf /etc/init/fake-container-events.conf  
  
# Setup apt to be happy with no console input  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup apt tools and other goodies we want  
RUN apt-get update && apt-get -y install apt-utils wget curl htop iputils-ping
vim-nox less debconf-utils w3m ssh  
  
# add owncloud repository and install  
RUN sh -c "echo 'deb
http://download.opensuse.org/repositories/isv:/ownCloud:/community/xUbuntu_14.04/
/' >> /etc/apt/sources.list.d/owncloud.list"  
  
# Fix authentication issues  
RUN wget
http://download.opensuse.org/repositories/isv:ownCloud:community/xUbuntu_14.04/Release.key  
RUN sudo apt-key add - < Release.key  
RUN apt-get update --fix-missing  
RUN apt-get -y upgrade  
  
# Assuming sqlite is used, not mysql or postgresql  
# Install owncloud  
RUN apt-get install -y owncloud  
  
# Get Upstart binary working. We remove a fake symlink to initctl and restore
the original.  
RUN rm /sbin/initctl; dpkg-divert --rename --remove /sbin/initctl  
  
# generate a nice UTF-8 locale for our use  
# RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8  
# Remove some services that don't make sense in containers.  
RUN /usr/sbin/update-rc.d -f ondemand remove; \  
for f in \  
/etc/init/u*.conf \  
/etc/init/mounted-dev.conf \  
/etc/init/mounted-proc.conf \  
/etc/init/mounted-run.conf \  
/etc/init/mounted-tmp.conf \  
/etc/init/mounted-var.conf \  
/etc/init/hostname.conf \  
/etc/init/tty*.conf \  
/etc/init/plymouth*.conf \  
/etc/init/hwclock*.conf \  
/etc/init/module*.conf\  
; do \  
dpkg-divert --local \--rename --add "$f"; \  
done; \  
echo '# /lib/init/fstab: cleared out for bare-bones Docker' > /lib/init/fstab  
  
# allow login with password  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# let Upstart know it's in a container  
ENV container docker  
  
# set an INSECURE password  
RUN echo 'root:toor' | chpasswd  
  
# Startup Scripts  
ADD setupScripts/rc.local /etc/rc.local  
RUN chmod 755 /etc/rc.local  
  
# ports 80 and 443 should be published in the command to the host!  
EXPOSE 22  
EXPOSE 80  
EXPOSE 443  
# Set up init  
CMD ["/sbin/init"]  

