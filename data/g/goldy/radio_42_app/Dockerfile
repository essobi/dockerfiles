FROM debian:stretch  
  
CMD ["/usr/bin/supervisord", "-n"]  
  
ADD 02apt-no-recom /etc/apt/apt.conf.d/  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get -y install nginx
at ca-certificates bzip2 \  
emacs24-nox faad flac git htop id3v2 id3 lame libav-tools \  
mpc mpd ncmpcpp php-cli php-fpm pulseaudio sox \  
supervisor swh-plugins vlc-nox vorbis-tools wget net-tools  
  
ADD init /init  
ADD mpd.conf /etc/mpd.conf  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD system.pa /etc/pulse/system.pa  
ADD daemon.conf /etc/pulse/daemon.conf  
ADD nginx.conf /etc/nginx/sites-available/radio42  
ADD silent.ogg /silent.ogg  
RUN ln -s /etc/nginx/sites-available/radio42 /etc/nginx/sites-enabled/radio42  
RUN rm /etc/nginx/sites-enabled/default  
RUN mkdir /run/php  
ADD opt /opt  
  
RUN mkdir -p /var/www/radio42/  
RUN chown www-data:www-data /var/www/radio42/  
RUN chown pulse:pulse /var/lib/mpd  
USER www-data  
RUN git clone https://github.com/cmehay/radio_42.git -b docker
/var/www/radio42/  
  
VOLUME /music  
VOLUME /playlist  
VOLUME /var/lib/mpd  
  
USER root  
  
RUN adduser mpd pulse  
  
EXPOSE 80 8080 6600  

