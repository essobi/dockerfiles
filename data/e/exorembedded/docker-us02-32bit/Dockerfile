FROM 32bit/ubuntu:14.04  
MAINTAINER Exor info@exorembedded.it  
  
# Use bash insted of sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install required packages and setup source repositories (required to patch
pam)  
RUN cat /etc/apt/sources.list | sed s/deb/deb-src/ >> /etc/apt/sources.list  
RUN apt-get update && apt-get install -y git python diffstat texinfo gawk
chrpath wget nano  
RUN apt-get install -y build-essential sudo  
RUN apt-get install -y x11vnc xvfb xinit bc g++-multilib  
  
# Fake initscripts  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN dpkg-divert --local \--rename --add /etc/init.d/systemd-logind  
RUN ln -sf /bin/true /sbin/initctl  
RUN ln -sf /bin/true /etc/init.d/systemd-logind  
RUN apt-get install -y e17  
  
# Setup avahi to autoconnect to device  
RUN apt-get install -y avahi-daemon avahi-utils  
EXPOSE 5353/udp  
RUN mkdir -p /var/run/dbus  
  
# to use avahi in with --net host we need to rebuild pam with disable-audit to
due a kernel bug solved in kernels > 3.15  
#Setup build environment for libpam  
RUN apt-get -y build-dep pam  
#Rebuild and istall libpam with --disable-audit option  
RUN export CONFIGURE_OPTS=--disable-audit && cd /root && apt-get -b source pam
&& dpkg -i libpam-doc*.deb libpam-modules-bin*.deb libpam-runtime*.deb
libpam0g*.deb && dpkg -i libpam-modules_1.1.8-1ubuntu2.2_i386.deb  
  
# gstreamer qtcreator deps  
RUN sudo apt-get install -y libgstreamer0.10-0 libgstreamer-plugins-base0.10-0  
  
# Trigger a cache cleanup changing version number  
RUN echo 1.1 > /boot/vmVersion  
  
# Install SDK  
RUN wget https://copy.com/JNh9V08fl4AH17h4/us02-public/exor-alterakit-
sdk-i386.sh?download=1 -O /exor-alterakit-sdk.sh  
RUN chmod +x /exor-alterakit-sdk.sh  
RUN /exor-alterakit-sdk.sh  
RUN rm -f /exor-alterakit-sdk.sh  
  
# Bitbake wont run as root, create a new user and home folder  
RUN useradd -m -d /home/user -s /bin/bash user && echo "user:password" |
chpasswd && adduser user sudo  
RUN chown -R user:user /home/user  
  
# Change user  
USER user  
ENV HOME /home/user  
# Install qtcreator  
RUN wget https://copy.com/JNh9V08fl4AH17h4/us02-public/qtcreator-
docker-3.3.2.tar.gz?download=1 -O /home/user/qtcreator-3.3.2.tar.gz  
RUN tar xpzf ~/qtcreator-3.3.2.tar.gz -C ~/ && rm ~/qtcreator-3.3.2.tar.gz  
  
# Clone repositories  
RUN mkdir -p ~/yocto-1.5.3/git  
WORKDIR /home/user/yocto-1.5.3/git  
RUN git clone -b exorint git://github.com/ExorEmbedded/yocto-poky.git  
RUN git clone -b exorint git://github.com/ExorEmbedded/yocto-meta-
openembedded.git  
RUN git clone -b dora git://github.com/ExorEmbedded/meta-browser.git  
RUN git clone -b master git://github.com/ExorEmbedded/meta-exor-us02.git  
RUN echo 'BUILD_ARCH = "i686"' >> meta-exor-us02/conf/local.conf.sample  
  
# Set yocto config template path  
ENV TEMPLATECONF /home/user/yocto-1.5.3/git/meta-exor-us02/conf  
  
# Apply settings and customizations  
COPY data/e17-settings.tar.gz /home/user/e17-settings.tar.gz  
COPY data/qtcreator-3.3.2-settings.tar.gz
/home/user/qtcreator-3.3.2-settings.tar.gz  
RUN tar xvzpf ~/e17-settings.tar.gz -C ~/ && rm ~/e17-settings.tar.gz  
RUN tar xvzpf ~/qtcreator-3.3.2-settings.tar.gz -C ~/ && rm
~/qtcreator-3.3.2-settings.tar.gz  
  
# Start VNC and desktop  
RUN echo -e "x11vnc -forever -nopw -display :9 -rfbport 5555 & \n
enlightenment_start \n" >> ~/.xinitrc  
RUN mkdir ~/.vnc  
  
# Export port 5555 to the host for VNC connection  
EXPOSE 5555  
# Export port 5353 to the host for mdns  
EXPOSE 5353  
USER root  
  
# Set user home as volume  
VOLUME /home/user/share  
  
# sample helloworld project  
COPY data/helloworld /home/user/helloworld  
RUN chown -R user:user /home/user/helloworld  
  
# welcome message  
COPY data/.bashrc /home/user/.bashrc  
RUN chown user:user /home/user/.bashrc  
  
# screen logo  
COPY data/Pattern_Radial.edj
/usr/share/enlightenment/data/backgrounds/Pattern_Radial.edj  
RUN chown user:user
/usr/share/enlightenment/data/backgrounds/Pattern_Radial.edj  
  
# cleanup  
#RUN apt-get clean  
#RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
WORKDIR /home/user  
CMD bash -c 'exec &> /dev/null ; dbus-daemon --system; avahi-daemon --no-drop-
root -D; su user -c "rm -f /tmp/.X9-lock; /usr/bin/xinit -- /usr/bin/Xvfb :9
-screen 0 1280x768x24 & "'; su user  

