FROM gentoo/stage3-amd64:20171030  
  
MAINTAINER Simon Lapin <lapinsa42@gmail.com>  
  
ADD http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2 /usr  
  
RUN mkdir -p /usr/portage/distfiles /usr/portage/metadata
/usr/portage/packages \  
&& emerge-webrsync \  
&& echo "MAKEOPTS=\"-j32\"" >> /etc/portage/make.conf \  
&& sed -ri 's/bindist/-bindist/g' /etc/portage/make.conf  

