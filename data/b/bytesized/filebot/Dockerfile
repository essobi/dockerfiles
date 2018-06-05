FROM bytesized/debian-base  
  
# Speed up APT  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update && \  
apt-get install -y oracle-java8-installer inotify-tools && \  
mkdir /app/  
  
RUN wget -O /app/filebot.deb
'https://app.filebot.net/download.php?type=deb&arch=amd64&version=4.7.9' && \  
dpkg -i /app/filebot.deb && rm /app/filebot.deb  
  
ADD monitor.sh /app/monitor.sh  
  
RUN chmod +x /app/monitor.sh  
  
VOLUME /config /host  
  
COPY static /  

