FROM jokke/ubuntu-mate-x2go-desktop  
  
USER root  
  
# set correct environment variables  
ENV USER=mythtv \  
DEBIAN_FRONTEND=noninteractive \  
TERM=xterm  
  
# add repositories  
RUN add-apt-repository universe -y && \  
apt-add-repository ppa:mythbuntu/0.28 -y && \  
  
apt-get update -qq && \  
  
# install mythtv-backend, database and ping util  
apt-get install -y --no-install-recommends mythtv-backend mythtv-database
iputils-ping && \  
  
# create/place required files/folders  
mkdir -p /home/mythtv/.mythtv /var/lib/mythtv /var/log/mythtv /var/run/mysqld
/root/.mythtv \  
/mnt/movies /mnt/recordings && \  
  
# set a password for user mythtv and add to required groups  
echo "mythtv:mythtv" | chpasswd && \  
usermod -s /bin/bash -d /home/mythtv -a -G users,mythtv,adm,sudo mythtv && \  
  
# set permissions for files/folders  
chown -R mythtv:users /var/lib/mythtv /var/log/mythtv /mnt/recordings
/mnt/movies && \  
# clean up  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
/usr/share/man /usr/share/groff /usr/share/info \  
/usr/share/lintian /usr/share/linda /var/cache/man && \  
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) &&
\  
(( find /usr/share/doc -empty|xargs rmdir || true ))  
  
# change logging  
RUN sed -i "s/syslog\ local7/logpath \/var\/log\/mythtv/g" /etc/init.d/mythtv-
backend && \  
update-rc.d mythtv-backend defaults  
  
# TODO, move above  
RUN apt-get update -qq && apt-get install -y mythtv-theme-mythbuntu  
  
# expose ports (UPnP, MythTV backend + API)  
EXPOSE 5000/udp 6543 6544  
  
COPY ["config.xml", "/etc/mythtv/"]  
RUN chown mythtv:mythtv /etc/mythtv/config.xml  

