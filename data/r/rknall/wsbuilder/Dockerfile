FROM phusion/baseimage:0.9.19  
MAINTAINER Roland Knall <rknall@gmail.com>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
run locale-gen en_US.UTF-8 &&\  
apt-get -q update &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openssh-server &&\  
apt-get -q autoremove &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get -q update &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openjdk-9-jre-headless build-essential
automake autoconf libgtk2.0-dev libglib2.0-dev libpcap0.8-dev flex bison
liblua5.2-0 liblua5.2-dev lua5.2 qt5-default cmake zlib1g zlib1g-dev git
qttools5-dev-tools libqt5multimedia5 libqt5multimedia5-plugins libqt5svg5
libqt5svg5-dev libqt5printsupport5 libc-ares-dev libc-ares2 libssh-dev
libssh-4 &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
RUN useradd -m -d /home/jenkins -s /bin/bash jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
#RUN mkdir /home/jenkins/.ssh  
#RUN ssh-keygen -f /home/jenkins/.ssh2/ida_rsa -t rsa -N ''  
EXPOSE 22  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/usr/sbin/sshd", "-D"]

