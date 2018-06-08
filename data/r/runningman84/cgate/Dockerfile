FROM ubuntu:18.04  
MAINTAINER Philipp Hellmich <phil@hellmi.de>  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/runningman84/docker-cgate"  
  
ENV MAILSERVER_DOMAIN=example.org \  
MAILSERVER_HOSTNAME=mail.example.org \  
HELPER_THREADS=3 \  
CGPAV_SPAMASSASIN_HOST=localhost \  
CGPAV_SPAMASSASIN_PORT=783 \  
CGPAV_SPAM_ACTION=addheaderjunk \  
CGPAV_EXTRA_SPAM_ACTION=reject \  
CGPAV_EXTRA_SPAM_SCORE=10 \  
CGPAV_VIRUS_ACTION=none  
  
# Install wget  
RUN apt-get update && \  
apt-get -y install wget curl && \  
rm -rf /var/lib/apt/lists/*  
  
# install dumb init  
RUN wget -q https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64.deb && \  
dpkg -i dumb-init_*.deb && rm dumb-init_*.deb  
  
# add our user to make sure their IDs get assigned consistently, regardless of
whatever dependencies get added  
RUN useradd -r cgatepro -d /var/CommuniGate -g mail \  
&& mkdir -p /var/CommuniGate \  
&& chown -R cgatepro.mail /var/CommuniGate  
  
# install communigate 32bit static  
#RUN cd /tmp \  
#&& wget -q ftp://ftp.stalker.com/pub/CommuniGatePro/CGatePro-Linux-Intel.tgz
\  
#-O /tmp/CGatePro-Linux-Intel.tgz \  
#&& tar -xzf /tmp/CGatePro-Linux-Intel.tgz \  
#&& mv /tmp/CGateProSoftware/CommuniGate /opt/ \  
#&& rm -fr /tmp/CGateProSoftware/ \  
#&& rm /tmp/CGatePro-Linux-Intel.tgz \  
#&& rm /opt/CommuniGate/CGServer \  
#&& rm /opt/CommuniGate/mail \  
#&& rm /opt/CommuniGate/sendmail  
RUN cd /tmp \  
&& wget -q ftp://ftp.stalker.com/pub/CommuniGatePro/CGatePro-Linux_amd64.deb \  
-O /tmp/CGatePro-Linux_amd64.deb \  
&& dpkg -i /tmp/CGatePro-Linux_amd64.deb \  
&& rm -fr /tmp/*  
  
# install cgpav  
# http://program.farit.ru/antivir/cgpav-1.5.tar.gz  
ADD cgpav-64 /opt/CommuniGate/cgpav  
RUN chmod 755 /opt/CommuniGate/cgpav  
  
ADD Main.settings /opt/CommuniGate/SAMPLE/Main.settings  
ADD Rules.settings /opt/CommuniGate/SAMPLE/Rules.settings  
ADD Queue.settings /opt/CommuniGate/SAMPLE/Queue.settings  
  
ADD cgpav.conf /etc/cgpav.conf  
  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
# Define mountable directories.  
VOLUME ["/var/CommuniGate"]  
  
# Server CMD  
CMD ["dumb-init", "/run.sh"]  
  
# Expose ports.  
#cgate_1 | 19:54:55.527 2 HTTPU [0.0.0.0]:8100 listener ready for connections  
#cgate_1 | 19:54:55.527 2 HTTPA [0.0.0.0]:8010 listener ready for connections  
#cgate_1 | 19:54:55.527 2 HTTPA [0.0.0.0]:9010 listener ready for connections  
#cgate_1 | 19:54:55.528 2 HTTPU [0.0.0.0]:9100 listener ready for connections  
#cgate_1 | 19:54:55.528 2 PWD [0.0.0.0]:106 listener ready for connections  
#cgate_1 | 19:54:55.528 2 STUN [0.0.0.0]:3478 listener ready for connections  
#cgate_1 | 19:54:55.528 2 STUN [0.0.0.0]:5349 listener ready for connections  
#cgate_1 | 19:54:55.528 2 POP [0.0.0.0]:110 listener ready for connections  
#cgate_1 | 19:54:55.528 2 ACAP [0.0.0.0]:674 listener ready for connections  
#cgate_1 | 19:54:55.528 2 LDAP [0.0.0.0]:636 listener ready for connections  
#cgate_1 | 19:54:55.528 2 LDAP [0.0.0.0]:389 listener ready for connections  
#cgate_1 | 19:54:55.528 2 IMAP [0.0.0.0]:143 listener ready for connections  
#cgate_1 | 19:54:55.528 2 IMAP [0.0.0.0]:993 listener ready for connections  
#cgate_1 | 19:54:55.528 2 FTP [0.0.0.0]:8021 listener ready for connections  
#cgate_1 | 19:54:55.528 2 SMTP [0.0.0.0]:25 listener ready for connections  
#cgate_1 | 19:54:55.528 2 SIP [0.0.0.0]:5060 listener ready for connections  
#cgate_1 | 19:54:55.528 2 SIP [0.0.0.0]:5061 listener ready for connections  
#cgate_1 | 19:54:55.528 2 XMPP [0.0.0.0]:5222 listener ready for connections  
#cgate_1 | 19:54:55.528 2 XMPP [0.0.0.0]:5269 listener ready for connections  
#cgate_1 | 19:54:55.528 2 XIMSS [0.0.0.0]:11024 listener ready for connections  
EXPOSE 8100 8010 9010 9100 106 3478 5349 110 674 636 143 993 8021 25 5060/udp
5061/udp 5222 5269 11024  
HEALTHCHECK \--interval=5m --timeout=3s CMD curl -I -s -f
http://localhost:8100/ || exit 1  

