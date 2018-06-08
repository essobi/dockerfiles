# docker build -t gbevan/pastmonsensor .  
#  
# to run: see pastmon-sensor@.service example coreos unit file.  
#  
  
FROM ubuntu:trusty  
MAINTAINER Graham Bevan "graham.bevan@ntlworld.com"  
  
ENV DEBIAN_FRONTEND=noninteractive \  
LANG=C \  
LC_ALL=C  
  
RUN \  
apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y wget aptitude htop vim git traceroute dnsutils \  
curl sudo psmisc gcc make build-essential pkg-config \  
libglib2.0-dev libpcap-dev libdbi-dev libdbd-pgsql flex \  
sysstat bison packaging-dev tree \  
libpcre3-dev sysstat tcpdump  
  
RUN \  
useradd --create-home -s /bin/bash pastmon && \  
echo -n 'pastmon:pastmon' | chpasswd && \  
mkdir -p /etc/sudoers.d && \  
echo "pastmon ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/pastmon && \  
chmod 0440 /etc/sudoers.d/pastmon && \  
echo "set modeline" > /etc/vim/vimrc.local && \  
echo "export TERM=vt100\nexport LANG=C\nexport LC_ALL=C" >
/etc/profile.d/dockenv.sh && \  
echo "export TERM=vt100\nexport LANG=C\nexport LC_ALL=C" >> /root/.bashrc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
su - pastmon -c "git clone git://git.code.sf.net/p/pastmon/pastmon pastmon" &&
\  
su - pastmon -c "\  
cd pastmon/PasTmon && \  
./bootstrap $* && make && sudo make install \  
"  
  
ADD start-pastmon-sensor.sh /usr/local/pastmon/bin/  
  
ENTRYPOINT ["/bin/bash", "/usr/local/pastmon/bin/start-pastmon-sensor.sh"]  

