FROM phusion/baseimage:0.9.16  
MAINTAINER Capt.Insano  
  
# Set correct environment variables  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LD_LIBRARY_PATH=/usr/local/tonido  
  
# Configure user nobody to match unRAID's settings  
RUN \  
usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /config nobody && \  
chown -R nobody:users /home  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
#Make Directory for Tonido  
RUN mkdir /usr/local/tonido  
  
#Install Tonido  
RUN \  
apt-get update -q && \  
apt-get -qy install\  
wget\  
tmux\  
libjpeg8\  
libfontconfig1\  
curl && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
cd /usr/local/tonido && \  
wget -U 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101
Firefox/36.0' -O tonido64.tar.gz
http://www.tonido.com/download.php?tonido64.tar.gz && \  
tar -zxvf tonido64.tar.gz && \  
rm tonido64.tar.gz  
  
#Make Directory to mount unRAID filesystem  
RUN mkdir /unRAID /config  
  
#Expose Volumes  
VOLUME /unRAID /config  
  
# Expose Port  
EXPOSE 10001  
# Add firstrun.sh to execute during container startup  
ADD firstrun.sh /etc/my_init.d/firstrun.sh  
RUN chmod +x /etc/my_init.d/firstrun.sh  
  
# Add tonido to runit  
RUN mkdir /etc/service/tonido  
ADD tonido.sh /etc/service/tonido/run  
RUN chmod +x /etc/service/tonido/run  
  
CMD ["/sbin/my_init"]  

