FROM phusion/baseimage:0.9.22  
MAINTAINER Enrico Maria Carmona, e.carmona@asst-monza.it  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# https://github.com/phusion/baseimage-docker#upgrading_os  
RUN apt-get update \  
&& apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
# Fix locale issue, see https://github.com/phusion/baseimage-docker/issues/276  
RUN locale-gen it_IT.UTF-8  
ENV LANG=it_IT.UTF-8 \  
LANGUAGE=it:en \  
LC_ALL=it_IT.UTF-8  
# https://github.com/phusion/baseimage-docker#security  
RUN chmod 755 /etc/container_environment \  
&& chmod 644 /etc/container_environment.sh /etc/container_environment.json  
  
# SSH  
# https://github.com/phusion/baseimage-docker#enabling-ssh  
RUN rm -f /etc/service/sshd/down  
  
# Disable tunnelled clear text passwords  
RUN sed -i 's/#PasswordAuthentication/PasswordAuthentication/'
/etc/ssh/sshd_config \  
&& sed -i 's/#UsePAM/UsePAM/' /etc/ssh/sshd_config \  
&& sed -i '/PasswordAuthentication/s/yes/no/g' /etc/ssh/sshd_config \  
&& sed -i '/UsePAM/s/yes/no/g' /etc/ssh/sshd_config  
  
# Expose the SSH port  
EXPOSE 22  
# Add user "user"  
RUN adduser --disabled-password --gecos "User" \--uid 1000 user  
  
# Allow ssh connection adding your public key in container's
/home/user/.ssh/authorized_keys  
# docker exec -i my-x11-xpra /bin/bash -c 'cat >
/home/user/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub  
RUN mkdir -p /home/user/.ssh/  
  
# winswitch  
# from https://github.com/retog/docker-x11-xpra/blob/master/Dockerfile  
RUN curl https://winswitch.org/gpg.asc | apt-key add - \  
&& echo "deb http://winswitch.org/ xenial main" >
/etc/apt/sources.list.d/winswitch.list  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
# https://packages.debian.org/en/jessie/i3  
i3 \  
# https://packages.debian.org/en/jessie/nano  
nano \  
# https://packages.debian.org/en/jessie/rox-filer  
rox-filer \  
# https://packages.debian.org/jessie/x11-apps  
x11-apps \  
# https://packages.debian.org/en/jessie/xpra  
xpra \  
# https://packages.debian.org/en/jessie/xserver-xephyr  
xserver-xephyr \  
# https://packages.debian.org/en/jessie/xterm  
xterm  
  
ENV TERM=xterm \  
DISPLAY=:100  
ADD xpra-display /tmp/xpra-display  
RUN echo "$(cat /tmp/xpra-display)\n$(cat /etc/bash.bashrc)" >
/etc/bash.bashrc  
  
# Start xpra service  
# https://github.com/phusion/baseimage-docker#running_startup_scripts  
RUN mkdir /etc/service/xpra  
ADD startup_xpra.sh /etc/service/xpra/run  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

