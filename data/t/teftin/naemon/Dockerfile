FROM debian:wheezy  
MAINTAINER Stan <teftin@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys F8C1CA08A57B9ED7  
RUN echo 'deb http://labs.consol.de/repo/stable/debian wheezy main' >
/etc/apt/sources.list.d/consol.list  
RUN apt-get update  
  
RUN apt-get install -y runit naemon-core naemon-tools naemon-livestatus thruk
nagios-plugins ssmtp nginx nagios-nrpe-plugin libfcgi-procmanager-perl
libapache2-mod-fcgid  
  
RUN rm /etc/nginx/sites-enabled/default  
ADD thruk.conf /etc/nginx/conf.d/  
ADD thruk_local.conf /etc/thruk/  
  
ADD sv /opt/sv  
  
VOLUME /naemon  
  
EXPOSE 80  
CMD exec runsvdir /opt/sv  

