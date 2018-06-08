FROM debian:wheezy  
  
RUN echo 'deb http://ftp.us.debian.org/debian/ wheezy main' >>
/etc/apt/sources.list &&\  
echo 'deb http://security.debian.org/ wheezy/updates main' >>
/etc/apt/sources.list &&\  
apt-get -y \--quiet update && apt-get -y \--quiet upgrade && apt-get -y
\--quiet install git curl &&\  
echo 'deb http://files.freeswitch.org/repo/deb/debian/ wheezy main' >>
/etc/apt/sources.list.d/freeswitch.list &&\  
curl http://files.freeswitch.org/repo/deb/debian/freeswitch_archive_g0.pub |
apt-key add -  
  
RUN apt-get -y \--quiet update && apt-get -y \--quiet install freeswitch  
freeswitch-mod-commands \  
freeswitch-mod-conference \  
freeswitch-mod-db \  
freeswitch-mod-dptools \  
freeswitch-mod-enum \  
freeswitch-mod-esf \  
freeswitch-mod-expr \  
freeswitch-mod-fifo \  
freeswitch-mod-fsv \  
freeswitch-mod-hash \  
freeswitch-mod-httapi \  
freeswitch-mod-sms \  
freeswitch-mod-spandsp \  
freeswitch-mod-valet-parking \  
freeswitch-mod-voicemail \  
freeswitch-mod-amr \  
freeswitch-mod-bv \  
freeswitch-mod-b64 \  
freeswitch-mod-g723-1 \  
freeswitch-mod-g729 \  
freeswitch-mod-h26x \  
freeswitch-mod-vp8 \  
freeswitch-mod-opus \  
freeswitch-mod-dialplan-xml \  
freeswitch-mod-rtc \  
freeswitch-mod-verto \  
freeswitch-mod-loopback \  
freeswitch-mod-skinny \  
freeswitch-mod-sofia \  
freeswitch-mod-cdr-csv \  
freeswitch-mod-event-socket \  
freeswitch-mod-local-stream \  
freeswitch-mod-native-file \  
freeswitch-mod-sndfile \  
freeswitch-mod-tone-stream \  
freeswitch-mod-lua \  
freeswitch-mod-console \  
freeswitch-mod-logfile \  
freeswitch-mod-syslog \  
freeswitch-mod-say-en \  
freeswitch-mod-xml-rpc \  
freeswtich-mod-xml-scgi \  
\  
freeswitch-mod-xml-curl \  
freeswitch-mod-flite \  
freeswitch-mod-directory \  
&& apt-get clean  
  
ENV FREESWITCH_PATH /etc/freeswitch  
  
# RUN useradd --system \--home-dir ${FREESWITCH_PATH} --comment "FreeSWITCH
Voice Platform" \--groups daemon freeswitch && \  
chown -R freeswitch:daemon ${FREESWITCH_PATH} && \  
chmod -R ug=rwX,o= ${FREESWITCH_PATH} && \  
chmod -R u=rwx,g=rx ${FREESWITCH_PATH}/bin/*  
  
CMD ["/usr/bin/freeswitch", "-nc"]  

