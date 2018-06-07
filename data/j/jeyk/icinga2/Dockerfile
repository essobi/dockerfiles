# Dockerfile for icinga2, icinga-web and icinga2-classicui  
FROM debian:wheezy  
  
MAINTAINER Joachim Breitsprecher  
  
# Environment variables  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update package lists.  
RUN apt-get -qq update  
  
# Install basic packages.  
RUN apt-get -qqy install --no-install-recommends sudo procps ca-certificates
wget pwgen  
  
# Install supervisord because we need to run Apache and Icinga2 at the same
time.  
RUN apt-get -qqy install --no-install-recommends supervisor  
  
# Add supervisord configuration  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Add debmon repository key to APT.  
RUN wget -O - http://debmon.org/debmon/repo.key 2>/dev/null | apt-key add -  
  
# Add Debian Backports and Debmon repositories and update package lists again.  
RUN echo "deb http://http.debian.net/debian wheezy-backports main" >>
/etc/apt/sources.list  
RUN echo "deb http://debmon.org/debmon debmon-wheezy main" >>
/etc/apt/sources.list  
RUN apt-get -qq update  
  
# When depencencies are pulled in by icinga-web, they seem to be configured
too late and configuration  
# of icinga-web fails. To work around this, install dependencies beforehand.  
RUN apt-get -qqy --no-install-recommends install apache2 mysql-client  
  
# Install icinga2 and icinga-classicui.  
RUN apt-get -qqy install --no-install-recommends icinga2 icinga2-ido-mysql
icinga-web icinga2-classicui nagios-plugins  
  
# Clean up some.  
RUN apt-get clean  
  
# Enable IDO for MySQL. This is needed by icinga-web.  
RUN icinga2-enable-feature ido-mysql  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
  
VOLUME ["/etc/icinga2"]  
  
# Initialize and run Supervisor  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/supervisord"]  

