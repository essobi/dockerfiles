FROM ubuntu:precise  
LABEL maintainer "Naresh Mehta (naresh.mehta@gmail.com)"  
LABEL Description="Yocto 1.8 Docker Build Evnrionment"
Vendor="https://www.naresh.se/" Version="0.0.1"  
  
ENV TERM=${TERM:-dumb}  
  
# Install yocto-1.8 specific things  
#USER root  
RUN apt-get -y update && apt-get -y install software-properties-common python-
software-properties  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test && apt-get -y update &&
apt-get install -y gawk wget git-core diffstat \  
unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev libtool
autoconf \  
xterm make git python tar libsdl-image1.2-dev libsdl-mixer1.2-dev m4 gettext
bitbake \  
patch g++ rpm zlib1g-dev m4 bison libncurses5-dev libglib2.0-dev ia32-libs
x11proto-core-dev \  
tcl intltool libxml2-dev liborbit2-dev libx11-dev ccache flex uuid-dev
liblzo2-dev libdbus-glib-1-dev libgtk2.0-dev libdbus-glib-1-dev \  
curl libsdl-ttf2.0-dev nano vim sudo gcc-5 g++-5 gcc-5-multilib g++-5-multilib
&& \  
ls -la /usr/bin/ | grep -oP "[\S]*(gcc|g\\+\\+)(-[a-z]+)*[\s]" | xargs bash -c
'for link in ${@:1}; do ln -s -f "/usr/bin/${link}-${0}" "/usr/bin/${link}";
done' 5  
  
EXPOSE 22  
RUN mkdir -p /var/run/sshd  
RUN chmod 0755 /var/run/sshd  
  
# Create and configure yocto user  
RUN useradd --create-home -s /bin/bash yocto  
  
RUN curl
http://downloads.yoctoproject.org/releases/yocto/yocto-1.8/buildtools/poky-
glibc-x86_64-buildtools-tarball-core2-64-buildtools-nativesdk-
standalone-1.8.sh -o x86_64-buildtools-nativesdk-standalone-1.8.sh && \  
chmod +x x86_64-buildtools-nativesdk-standalone-1.8.sh && \  
curl
http://downloads.yoctoproject.org/releases/yocto/yocto-1.8/toolchain/x86_64/poky-
glibc-x86_64-core-image-sato-armv7a-vfp-neon-toolchain-1.8.sh -o poky-
glibc-x86_64-core-image-sato-armv7a-vfp-neon-toolchain-1.8.sh && \  
chmod +x poky-glibc-x86_64-core-image-sato-armv7a-vfp-neon-toolchain-1.8.sh  
RUN sh ./x86_64-buildtools-nativesdk-standalone-1.8.sh -y -d
/home/yocto/buildtools && rm x86_64-buildtools-nativesdk-standalone-1.8.sh &&
\  
sh ./poky-glibc-x86_64-core-image-sato-armv7a-vfp-neon-toolchain-1.8.sh -y -d
/opt/poky/1.8 && rm poky-glibc-x86_64-core-image-sato-armv7a-vfp-neon-
toolchain-1.8.sh  
  
### Install required NodeJs 4.8.0  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && apt-get install
-y nodejs  
  
#RUN curl -L https://git.io/n-install -o n-install.sh && chmod +x n-install.sh
&& ./n-install.sh -y 4.8.0 && ln -sf /usr/local/n/versions/node/4.8.0/bin/node
/usr/bin/node && rm n-install.sh  
# Configure SSH access  
RUN mkdir -p /home/yocto/.ssh /home/yocto/project && \  
echo "ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ==
yocto insecure public key" > /home/yocto/.ssh/authorized_keys && \  
chown -R yocto: /home/yocto/.ssh && echo -n 'yocto:yocto' | chpasswd  
  
# Enable passwordless sudo for the "yocto" user  
RUN mkdir -p /etc/sudoers.d && \  
install -b -m 0440 /dev/null /etc/sudoers.d/yocto && \  
echo 'yocto ALL=NOPASSWD: ALL' >> /etc/sudoers.d/yocto  
  
# Maximize max_user_watches  
ADD 60-max-user-watches.conf /etc/sysctl.d/.  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install meteor as yocto user so it installs in ~  
USER yocto  
RUN curl https://install.meteor.com/ | sh  
  
### Install repo & append to path  
RUN mkdir -p /home/yocto/bin && \  
echo "export PATH=/home/yocto/bin:/home/yocto/.meteor:$PATH" >>
/home/yocto/.bashrc && echo "export TERM=${TERM:-dumb}" >> /home/yocto/.bashrc
&& \  
curl https://storage.googleapis.com/git-repo-downloads/repo >
/home/yocto/bin/repo && chmod a+x /home/yocto/bin/repo  
  
VOLUME /home/yocto/project  
WORKDIR /home/yocto  
  
CMD "/bin/bash"  

