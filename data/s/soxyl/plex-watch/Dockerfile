FROM ubuntu  
  
MAINTAINER Samuel Wicky <samuel.wicky@avq.ch>  
  
RUN apt-get update -q && \  
apt-get install -y -q libwww-perl libxml-simple-perl libtime-duration-perl
libtime-modules-perl libdbd-sqlite3-perl perl-doc libjson-perl && \  
apt-get install -y -q wget && \  
wget -P /opt/plexWatch/
https://raw.github.com/ljunkie/plexWatch/master/plexWatch.pl && \  
wget -P /opt/plexWatch/
https://raw.github.com/ljunkie/plexWatch/master/config.pl-dist && \  
cat /opt/plexWatch/config.pl-dist | \  
sed "s/\$server = 'localhost';/\$server = 'plex';/" | \  
sed "s/\$data_dir = '\/opt\/plexWatch\/';/\$data_dir = '\/data\/';/" > \  
/opt/plexWatch/config.pl && \  
chmod +x /opt/plexWatch/plexWatch.pl  
  
COPY start.sh /start.sh  
  
RUN chmod +x /start.sh  
  
ENTRYPOINT /start.sh  
  
VOLUME /data  

