FROM ubuntu:14.04.2  
# Derived from jplock/rsyslog  
# Credit to original maintainer Justin Plock <justin@plock.net>  
# We just add volumes and some templates to the image  
MAINTAINER Stephan Buys <stephan.buys@panoptix.co.za>  
  
ENV REFRESHED_ON "08 Jul 2015"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y -q upgrade  
RUN apt-get -y -q install software-properties-common python-software-
properties  
RUN add-apt-repository ppa:adiscon/v8-stable  
RUN apt-get update && apt-get -y -q install rsyslog  
  
RUN sed 's/#$ModLoad imudp/$ModLoad imudp/' -i /etc/rsyslog.conf  
RUN sed 's/#$UDPServerRun 514/$UDPServerRun 514/' -i /etc/rsyslog.conf  
RUN sed 's/#$ModLoad imtcp/$ModLoad imtcp/' -i /etc/rsyslog.conf  
RUN sed 's/#$InputTCPServerRun 514/$InputTCPServerRun 514/' -i
/etc/rsyslog.conf  
RUN sed 's/$ModLoad imklog/#$ModLoad imklog/' -i /etc/rsyslog.conf  
RUN sed 's/$FileOwner syslog/$FileOwner root/' -i /etc/rsyslog.conf  
RUN sed 's/$PrivDropToUser syslog/#$PrivDropToUser syslog/' -i
/etc/rsyslog.conf  
RUN sed 's/$PrivDropToGroup syslog/#$PrivDropToGroup syslog/' -i
/etc/rsyslog.conf  
  
ADD start.sh /usr/local/bin/  
ADD hostslogs.conf /etc/rsyslog.d/  
  
EXPOSE 514/tcp 514/udp  
VOLUME ["/var/log/hosts"]  
  
ENTRYPOINT ["/usr/local/bin/start.sh"]  
CMD ["-n"]  

