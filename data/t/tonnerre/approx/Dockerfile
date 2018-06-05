FROM debian:stable  
LABEL maintainer Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
# Tell apt to keep to itself.  
ENV DEBIAN_FRONTEND noninteractive  
ENV SETUID_USER approx  
ENV APPROX_LISTEN_PORT 8080  
# Build the sources.list cache.  
RUN apt-get -q -y update  
  
# Install esmtp so stuff stops installing exim.  
RUN apt-get -q -y -o Dpkg::Options::=--force-confdef -o
Dpkg::Options::=--force-confold --purge install esmtp esmtp-run  
  
# Ensure we can write syslogs.  
RUN apt-get -q -y -o Dpkg::Options::=--force-confdef -o
Dpkg::Options::=--force-confold --purge install rsyslog rsyslog-relp  
  
# Install approx, esmtp and the inetd to run approx from.  
RUN apt-get -q -y -o Dpkg::Options::=--force-confdef -o
Dpkg::Options::=--force-confold --purge install approx bzip2 openbsd-inetd
update-inetd  
  
# Set up rsyslog.  
COPY rsyslog.conf /etc/rsyslog.conf  
  
# Configure approx with some defaults.  
COPY approx.conf /etc/approx/approx.conf  
  
# Ensure we have the directories required for the volumes.  
RUN /usr/bin/install -o approx -g approx -m 0755 -d /srv/approx/cache  
  
# Install the run script. We have to run 2 commands at all times (launch  
# syslog, then start inetd), so we have to use a script.  
ADD run-inetd.sh /usr/local/bin/run-inetd.sh  
  
# It's an HTTP server.  
EXPOSE 8080/tcp  
  
# Config and cache directory is an obvious candidate for volumes.  
VOLUME ["/etc/approx", "/srv/approx/cache"]  
  
# Our main purpose will be to run inetd.  
CMD /bin/sh /usr/local/bin/run-inetd.sh  

