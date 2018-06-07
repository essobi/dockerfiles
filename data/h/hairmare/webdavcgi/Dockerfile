FROM hairmare/gentoo  
  
  
MAINTAINER Lucas Bickel <hairmare@purplehaze.ch>  
  
ENV GENTOO_WORLD_PACKAGES www-apps/webdavcgi dev-perl/SpeedyCGI app-
text/ghostscript-gpl  
  
# setup layman since we need that for now to get webdavcgi 1.0.0  
RUN emerge app-portage/layman -q  
RUN cd /etc/layman/overlays; wget https://raw.github.com/dev-zero/gentoo-
proxy-maintenance-webdavcgi/master/layman/proxy-maintenance-webdavcgi.xml; sed
-i -e 's|/dev-zero/|/hairmare/|' proxy-maintenance-webdavcgi.xml  
RUN sed -i -e 's|^#overlay_defs|overlay_defs|' /etc/layman/layman.cfg  
RUN layman -S  
RUN layman -a proxy-maintenance-webdavcgi  
RUN echo 'source /var/lib/layman/make.conf' > /etc/portage/make.conf  
  
# install webdavcgi  
RUN emerge $GENTOO_WORLD_PACKAGES \--autounmask-write; etc-update -q
--automode -5  
RUN emerge $GENTOO_WORLD_PACKAGES -q  
  
# configure webdavcgi for SpeedyCGI  
RUN sed -i -e 's|#!/usr/bin/perl|#!/usr/bin/speedy -- -r50 -M7 -t3600|'
/usr/libexec/webdavcgi-*/cgi-bin/webdav.pl  
  
# configure apache  
RUN sed -i -e 's|^APACHE2_OPTS=.*|APACHE2_OPTS=""|' /etc/conf.d/apache2  
RUN cat /usr/share/doc/webdavcgi-1.0.0/apache-webdavcgi-1.0-example.conf.bz2 |
bunzip2 > /etc/apache2/vhosts.d/webdavcgi_vhost.include  
COPY vhost.conf /etc/apache2/vhosts.d/00_webdavcgi_vhost.conf  
RUN rc-update add apache2  
  
RUN eselect news read new  
  
CMD bash -c '/sbin/rc default && tailf /var/log/apache2/error_log'  
  
EXPOSE 80  

