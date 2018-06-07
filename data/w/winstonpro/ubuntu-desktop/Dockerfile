FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV USER root  
ENV TZ Asia/Shanghai  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends ubuntu-desktop && \  
apt-get install -y gnome-panel gnome-settings-daemon metacity nautilus gnome-
terminal && \  
apt-get install -y tightvncserver && \  
mkdir /root/.vnc  
##  
RUN apt-get install -y openssh-server supervisor git vim firefox ttf-wqy-
microhei libnet1-dev libpcap0.8-dev && \  
mkdir /var/run/sshd && \  
echo 'root:root' |chpasswd && \  
sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config &&
\  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
##  
COPY supervisord.conf /etc/supervisord.conf  
##  
COPY reset.sh /root/reset.sh  
COPY check.sh /root/check.sh  
COPY vnc.sh /root/.vnc/vnc.sh  
RUN chmod +x /root/*.sh /root/.vnc/vnc.sh && \  
git clone https://github.com/snooda/net-speeder.git net-speeder  
WORKDIR net-speeder  
RUN sh build.sh && \  
mv net_speeder /usr/local/bin/  
  
ADD xstartup /root/.vnc/xstartup  
ADD passwd /root/.vnc/passwd  
  
ADD entrypoint.sh /usr/sbin  
RUN chmod 600 /root/.vnc/passwd && \  
chmod +x /usr/sbin/entrypoint.sh /usr/local/bin/net_speeder  
WORKDIR /root  
  
EXPOSE 22 5901 443 80  
ENTRYPOINT ["entrypoint.sh"]  

