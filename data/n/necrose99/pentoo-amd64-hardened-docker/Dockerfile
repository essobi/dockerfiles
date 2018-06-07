FROM gentoo/stage3-amd64-hardened  
  
MAINTAINER necrose99 necrose99@protmail.ch mike@michaellawrenceit.com  
  
#ADD http://www.busybox.net/downloads/binaries/latest/busybox-i686 /busybox  
# This one should be present by running the build.sh script  
RUN echo "Getting layman"  
RUN emerge -v layman  
RUN layman -S && layman -a pentoo  
RUN eslect profile set pentoo:pentoo/hardened/linux/amd64/bleeding_edge  
RUN pentoo-updater  
  
  
  

