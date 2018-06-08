FROM marthym/base:jessie  
MAINTAINER marthym@github.com  
  
ENV GENS_VERSION 2.16.7  
# Install 32b dependency  
RUN dpkg --add-architecture i386 && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get -y update && \  
apt-get -y install libc6-i386 xdg-utils libgl1-mesa-glx:i386
libsdl1.2debian:i386 libglib2.0-0:i386 libgtk2.0-0:i386  
  
# Install SSH Server with X11 Forward  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get -y install openssh-server xauth && \  
mkdir /var/run/sshd  
ADD conf/sshd_config /etc/ssh/sshd_config  
  
# Install Gens/GS  
RUN wget http://segaretro.org/images/7/75/Gens_${GENS_VERSION}_i386.deb && \  
dpkg --force-architecture -i Gens_${GENS_VERSION}_i386.deb && \  
rm Gens_${GENS_VERSION}_i386.deb  
  
# Add services  
ADD services /etc/sv  
RUN chmod +x /etc/sv/**/run  
  
# add user gens  
RUN useradd gens --home /home/gens/ && \  
echo 'gens:gens' |chpasswd && \  
mkdir -p /home/gens/.ssh && \  
chmod 755 /home/gens/.ssh && \  
chown -Rf gens. /home/gens && \  
mkdir -p /home/gens/roms  
  
EXPOSE 22  
VOLUME /home/gens/roms  
  
# Clean up APT when done.  
RUN apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

