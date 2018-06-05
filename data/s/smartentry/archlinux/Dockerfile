FROM pritunl/archlinux  
  
MAINTAINER Yifan Gao <docker@yfgao.com>  
  
ENV ASSETS_DIR="/opt/smartentry/HEAD"  
COPY smartentry.sh /sbin/smartentry.sh  
  
COPY mirrorlist /etc/pacman.d/  
  
ENTRYPOINT ["/sbin/smartentry.sh"]  
  
CMD ["run"]  

