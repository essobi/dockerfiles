FROM ubuntu:latest  
MAINTAINER James Jones <velocity303@gmail.com>  
  
RUN echo 'deb http://download.videolan.org/pub/debian/stable/ /' >>
/etc/apt/sources.list  
RUN echo 'deb-src http://download.videolan.org/pub/debian/stable/ /' >>
/etc/apt/sources.list  
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty main multiverse' >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install --no-install-recommends -q -y wget  
RUN wget -O - http://download.videolan.org/pub/debian/videolan-apt.asc|sudo
apt-key add -  
RUN apt-get update  
RUN apt-get install --no-install-recommends -q -y apache2 php5 php5-json curl
php5-curl php5-mysql lame libvorbis-dev vorbis-tools flac libmp3lame-dev
libavcodec-extra* libfaac-dev libtheora-dev libvpx-dev libav-tools  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/www/*  
RUN cd /var/tmp \  
&& curl -sSL --insecure
https://github.com/ampache/ampache/archive/3.7.0.tar.gz | tar xz \  
&& mv /var/tmp/ampache-3.7.0/* /var/www/ \  
&& rm -rf /var/tmp/ampache-3.7.0 \  
&& chown -R www-data:www-data /var/www/  
  
ADD 001-ampache.conf /etc/apache2/sites-available/  
RUN rm -rf /etc/apache2/sites-enabled/*  
RUN ln -s /etc/apache2/sites-available/001-ampache.conf /etc/apache2/sites-
enabled/  
RUN a2enmod rewrite  
VOLUME ["/media"]  
VOLUME ["/var/www/config"]  
VOLUME ["/var/www/themes"]  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  

