FROM ubuntu-debootstrap:trusty  
MAINTAINER stauraum <kai.schubert@systemmanager.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV _clean="rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*"  
ENV _apt_clean="eval apt-get clean && $_clean"  
ENV TIMEZONE="Europe/London"  
# Set your local timezone  
RUN echo $TIMEZONE > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# fix locale  
RUN locale-gen en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LANGUAGE en_GB:gb  
ENV LC_ALL en_GB.UTF-8  
# Install s6-overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar zxf /tmp/s6-overlay-amd64.tar.gz -C / && $_apt_clean  
  
ENTRYPOINT [ "/init" ]  

