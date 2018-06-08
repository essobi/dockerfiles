FROM 32bit/debian:jessie  
  
MAINTAINER Gentoo Docker Team  
  
#ADD http://www.busybox.net/downloads/binaries/latest/busybox-i686 /busybox  
# This one should be present by running the build.sh script  
ADD build.sh /  
#ADD build-more.sh /  
RUN apt-get update && apt-get install -y \  
wget bzip2  
  
RUN /build.sh x86 i686  
  
# Setup the rc_sys  
RUN sed -e 's/#rc_sys=""/rc_sys="lxc"/g' -i /etc/rc.conf  
  
# By default, UTC system  
RUN echo 'UTC' > /etc/timezone  
  
#VOLUME ["${PORTAGE}:/usr/portage:rw",
"${PORTAGE}/distfiles:/usr/portage/distfiles:rw"]  
RUN mkdir /etc/portage/package.accept_keywords  
RUN mkdir -p /etc/portage/package.use  
# avoid a Python 2 dependency  
RUN echo 'dev-vcs/git -python' >> /etc/portage/package.use/layman  
RUN echo 'app-portage/layman ~x86' >>
/etc/portage/package.accept_keywords/layman  
# required by app-portage/layman-2.1.0-r2  
# =dev-python/ssl-fetch-0.2.1 ~amd64  
RUN echo 'dev-python/ssl-fetch ~x86' >>
/etc/portage/package.accept_keywords/layman  
  
RUN emerge -v layman  
RUN eselect news read new  
RUN echo 'source /var/lib/layman/make.conf' >> /etc/portage/make.conf  
RUN sed -i 's/^check_official.*/check_official : no/' /etc/layman/layman.cfg  
RUN layman --fetch  
RUN layman -a pentoo  
RUN eslect profile set pentoo:pentoo/default/linux/x86/bleeding_edge  
RUN pentoo-updater  
RUN echo "Bootstrapped Pentoo overlay into Docker / upadted & Happy
Hacking...."  

