FROM akohlbecker/base:latest  
  
RUN sed -i "/^# deb.*multiverse/ s/^# //" /etc/apt/sources.list && \  
echo "deb http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y software-properties-common python-software-properties git
unrar unzip p7zip par2 python-yenc && \  
add-apt-repository -y ppa:jcfp/nobetas && \  
add-apt-repository ppa:jcfp/sab-addons && \  
apt-get update && \  
apt-get install -y sabnzbdplus ffmpeg python-sabyenc && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
RUN apt-get update && \  
apt-get install -y locales && \  
locale-gen en_US.UTF-8 && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
ENV LANG en_US.UTF-8  
  
RUN git clone https://github.com/clinton-hall/nzbToMedia.git /opt/nzbToMedia  
  
RUN groupadd --gid 2000 media && \  
useradd --uid 2000 \--gid 2000 \--create-home media && \  
chown -R media:media /opt/nzbToMedia && \  
mkdir /data && \  
chown -R media:media /data  
USER media  
  
ADD app /app  
WORKDIR /app  
  
VOLUME ["/data"]  
  
EXPOSE 8080  
  
CMD ["/app/boot", "/usr/bin/sabnzbdplus", "--config-file", "/tmp/sabnzbd.ini",
"--console"]  

