FROM jacknlliu/ubuntu-init:14.04  
LABEL maintainer="Jack Liu <jacknlliu@gmail.com>"  
  
# setup environment  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
# install system packages  
RUN apt-get update -y \  
&& apt-get install -y -q --no-install-recommends apt-transport-https aptitude  
  
# install essential tools  
RUN aptitude install -y -q -R bash-completion wget vim git tmux terminator
xauth openssh-server runit sudo software-properties-common python-software-
properties debconf-utils policykit-1 xterm \  
\  
# setup ssh  
&& mkdir -p /var/run/sshd && echo "X11UseLocalhost no" >> /etc/ssh/sshd_config
\  
\  
# install URSim prerequisite  
&& dpkg --add-architecture i386 && aptitude update -y \  
&& aptitude install -y -q -R openjdk-6-jre openjdk-6-jdk libxmlrpc-c++8:i386 \  
&& echo "JAVA_HOME=\"/usr/lib/jvm/java-6-openjdk-amd64/jre/bin/java\"" >>
/etc/environment  
  
ENV JAVA_HOME /usr/lib/jvm/java-6-openjdk-amd64/jre/bin/java  
  
# install intel graphics driver  
RUN aptitude install -y -q -R libgl1-mesa-glx libgl1-mesa-dri \  
\  
# install amd graphics open source driver  
&& aptitude install -y -q -R mesa-vdpau-drivers xserver-xorg-video-ati mesa-
utils module-init-tools  
  
# set user ros and sudo  
RUN adduser --gecos "URSim User" \--home /home/ursim --disabled-password ursim
\  
&& usermod -a -G dialout ursim \  
&& echo "ursim ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/99_aptget \  
&& mkdir -p /opt/ursim  
  
# install ursim  
COPY scripts/install_ursim.sh /opt/ursim/  
RUN chmod -R a+rx /opt/ursim && sync && /opt/ursim/install_ursim.sh
"/opt/ursim/" "ursim" && rm -f /opt/ursim/install_ursim.sh && chmod -R a+rwx
/opt/ursim  
  
# aptitude clean  
RUN apt-get autoclean \  
&& apt-get clean all \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* /var/tmp/*  
  
ENV PATH /opt/ursim/ursimpkg:$PATH  
ENV URSIM_ROOT /opt/ursim/ursimpkg  
  
# redefine env for my_init  
RUN mkdir -p /etc/container_environment \  
&& echo "JAVA_HOME=\"/usr/lib/jvm/java-6-openjdk-amd64/jre/bin/java\"" >>
/etc/container_environment/JAVA_HOME \  
&& echo "PATH=\"/opt/ursim/ursimpkg:$PATH\"" >>
/etc/container_environment/PATH \  
&& echo "URSIM_ROOT=\"/opt/ursim/ursimpkg\"" >>
/etc/container_environment/URSIM_ROOT  
  
USER root  
WORKDIR /opt/ursim/ursimpkg  
# /sbin/my_init should be launched by root user  
ENTRYPOINT ["/sbin/my_init", "--quiet", "--", "setuser", "ursim"]  
CMD ["bash"]  

