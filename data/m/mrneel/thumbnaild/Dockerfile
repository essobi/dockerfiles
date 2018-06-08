FROM phusion/baseimage  
MAINTAINER Matt Neel <matt@mrneel.com>  
  
# Added by Mark based on https://github.com/phusion/baseimage-docker/issues/58  
ENV DEBIAN_FRONTEND noninteractive  
  
# Added by MH based on https://github.com/shincoder/homestead-docker/issues/5  
RUN printf "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d && \  
locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN apt-key update  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db  
  
# Prevent services from automatically starting after installation  
RUN echo exit 101 > /usr/sbin/policy-rc.d && \  
chmod +x /usr/sbin/policy-rc.d  
  
# Setup base system  
RUN rm -fr /etc/apt/sources.list && touch /etc/apt/sources.list && \  
add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu trusty
universe" && \  
add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu trusty main
restricted universe multiverse" && \  
add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu trusty-updates
main restricted universe multiverse" && \  
add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu trusty-
backports main restricted universe multiverse" && \  
add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu trusty-security
main restricted universe multiverse" && \  
add-apt-repository -y "deb http://ftp.osuosl.org/pub/mariadb/repo/10.0/ubuntu
trusty main" && \  
apt-get update && \  
apt-get -y dist-upgrade  
  
# Install dependencies  
RUN apt-get install -y --no-install-recommends build-essential software-
properties-common libreoffice git python-dev python-pip libreoffice-script-
provider-python unoconv poppler-utils imagemagick netpbm default-jre  
  
# Install flask  
RUN pip install flask  
  
# Setup runit services  
RUN mkdir /etc/service/soffice  
ADD soffice.runit.conf /etc/service/soffice/run  
RUN chmod +x /etc/service/soffice/run  
  
RUN mkdir /etc/service/thumbnaild  
ADD thumbnaild.runit.conf /etc/service/thumbnaild/run  
RUN chmod +x /etc/service/thumbnaild/run  
  
# Enable SSH  
RUN rm -f /etc/service/sshd/down  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Pull in application  
RUN git clone https://github.com/mattneel/thumbnaild.git /thumbnaild  
# Expose webservice port  
EXPOSE 8001  
# Execute runit  
CMD ["/sbin/my_init"]

