FROM ubuntu:xenial  
  
  
MAINTAINER Marcin Matlag "marcin.matlag@gmail.com"  
EXPOSE 16669  
user root  
  
ENV IRC_HOME /var/ircstack  
RUN mkdir -p "$IRC_HOME"  
  
ARG user=ircstack  
ARG group=ircstack  
ARG uid=1000  
ARG gid=1000  
RUN groupadd -g ${gid} ${group} \  
&& useradd -d "$IRC_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}  
  
RUN chown ${user}:${group} "$IRC_HOME"  
VOLUME "$IRC_HOME"  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get install -y software-properties-common python-software-properties
wget curl  
  
RUN add-apt-repository ppa:teward/znc  
RUN echo 'deb http://code.bitlbee.org/debian/master/xenial/amd64 ./' >
/etc/apt/sources.list.d/bitlbee.list  
RUN echo 'deb
http://download.opensuse.org/repositories/home:/jgeboski/xUbuntu_16.04 ./' >
/etc/apt/sources.list.d/bitlbee-facebook.list  
  
RUN wget -O- https://code.bitlbee.org/debian/release.key | apt-key add -  
RUN wget -O- https://jgeboski.github.io/obs.key | apt-key add -  
  
RUN apt-get update  
  
RUN apt-get install -y znc bitlbee bitlbee-facebook znc-dev  
  
RUN apt-get install -y libssl-dev automake gettext g++ make git  
  
#install znc-palaver  
WORKDIR /root  
RUN git clone https://github.com/cocodelabs/znc-palaver.git  
WORKDIR /root/znc-palaver  
RUN git checkout `git describe --abbrev=0 --tags`  
RUN make  
RUN cp palaver.so /usr/lib/znc/palaver.so  
RUN rm -rf /root/znc-palaver  
  
#install znc playback  
WORKDIR /root  
RUN git clone https://github.com/jpnurmi/znc-playback.git  
WORKDIR /root/znc-playback  
RUN znc-buildmod playback.cpp  
RUN cp playback.so /usr/lib/znc/playback.so  
RUN rm -rf /root/znc-playback  
  
#install znc clientbuffer  
WORKDIR /root  
RUN git clone https://github.com/jpnurmi/znc-clientbuffer.git  
WORKDIR /root/znc-clientbuffer  
RUN znc-buildmod clientbuffer.cpp  
RUN cp clientbuffer.so /usr/lib/znc/clientbuffer.so  
RUN rm -rf /root/znc-clientbuffer  
  
#install znc chanfilter  
WORKDIR /root  
RUN git clone https://github.com/jpnurmi/znc-chanfilter  
WORKDIR /root/znc-chanfilter  
RUN znc-buildmod chanfilter.cpp  
RUN cp chanfilter.so /usr/lib/znc/chanfilter.so  
RUN rm -rf /root/znc-chanfilter  
  
RUN apt-get purge -y libssl-dev automake gettext g++ make git  
  
COPY run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
RUN mkdir -p /usr/local/ircstack  
RUN chmod 750 /usr/local/ircstack  
COPY znc.conf /usr/local/ircstack  
COPY bitlbee.conf /usr/local/ircstack  
RUN chmod 640 /usr/local/ircstack/*  
RUN chown -R root:${group} /usr/local/ircstack/  
  
RUN apt-get install -y supervisor  
  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
COPY znc_supervisord.conf /etc/supervisor/conf.d/znc.conf.disabled  
COPY bitlbee_supervisord.conf /etc/supervisor/conf.d/bitlbee.conf.disabled  
RUN chown -R ${user}:${group} /etc/supervisor/  
  
ENV TINI_VERSION v0.14.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc
/tini.asc  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \  
&& gpg --verify /tini.asc  
RUN chmod 500 /tini  
RUN chown ${user}:${group} /tini  
  
WORKDIR "$IRC_HOME"  
USER ${user}  
  
  
ENTRYPOINT [ "/tini", "--", "/usr/local/bin/run.sh" ]  

