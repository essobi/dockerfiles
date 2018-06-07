FROM ubuntu:14.04  
MAINTAINER Steve Kamerman <stevekamerman@gmail.com>  
LABEL Description="Rsyslog Container"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q update && apt-get -qy install \  
python-software-properties \  
software-properties-common \  
\  
&& add-apt-repository -y ppa:adiscon/v8-stable \  
&& apt-get -q update && apt-get -qy install \  
rsyslog \  
\  
&& apt-get -qy remove --purge \  
python-software-properties \  
software-properties-common \  
&& apt-get -qy autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY resources/rsyslog.conf /etc/rsyslog.conf  
COPY resources/50-default.conf /etc/rsyslog.d/50-default.conf  
  
# Automatically mount this on your other containers with --volumes-from  
# There's a logging socket at /var/log/socket that you can symlink to /dev/log  
VOLUME /var/log  
  
# Or you can send your log data here with TCP or UDP  
EXPOSE 514/tcp 514/udp  
  
CMD ["/usr/sbin/rsyslogd", "-n", "-i", "/tmp/rsyslog.pid"]  
  

