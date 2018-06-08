FROM akohlbecker/base:latest  
  
RUN sed -i "/^# deb.*multiverse/ s/^# //" /etc/apt/sources.list && \  
echo "deb http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y unrar unzip p7zip git python2.7 && \  
git clone https://github.com/SickRage/SickRage.git /opt/sickrage && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
RUN groupadd --gid 2000 media && \  
useradd --uid 2000 --gid 2000 --create-home media && \  
chown -R media:media /opt/sickrage && \  
mkdir /data && \  
chown -R media:media /data  
USER media  
  
ADD app /app  
WORKDIR /app  
  
VOLUME ["/data"]  
  
EXPOSE 8081  
CMD ["/app/boot", "python2.7", "/opt/sickrage/SickBeard.py", "--nolaunch", "--
datadir=/data", "--config=/tmp/sickrage.ini"]  

