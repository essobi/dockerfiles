#  
# VERSION 1.0.1  
FROM westfalenyeti01/ubuntu-base  
MAINTAINER Björn Adler <bjoern@dnsgods.de>  
ENV DEBIAN_FRONTEND=noninteractive LANG=de_DE.UTF-8 LC_ALL=C.UTF-8
LANGUAGE=de_DE.UTF-8  
RUN add-apt-repository ppa:mc3man/xerus-media && add-apt-repository
ppa:ondrej/php && apt-get update  
RUN apt-get install -y nginx php7.0-common php7.0-cli php7.0-fpm
php7.0-sqlite3 php7.0-gd php7.0-mbstring ffmpeg lame libmp3lame0 git sqlite3  
RUN apt-get clean  
  
ADD etc_nginx.conf /etc/nginx/nginx.conf  
  
RUN cd /root; wget http://www.audiostreamer.org/AudioStreamer_v3_0_linux.zip;
unzip AudioStreamer_v3_0_linux.zip && mv /root/AudioStreamer /var/www  
RUN cd /var/www/AudioStreamer/core && rm -rf getid3 && git clone
https://github.com/JamesHeinrich/getID3.git getid3  
RUN chown -R www-data:www-data /var/www/AudioStreamer && chmod -R 770
/var/www/AudioStreamer  
  
VOLUME [ "/srv/audio" , "/var/www/AudioStreamer/sqlite" ]  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

