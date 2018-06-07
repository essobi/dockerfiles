# ARGUS  
#  
# VERSION 1.0  
FROM ubuntu  
MAINTAINER Jon Schipp <jonschipp@gmail.com>  
  
# Specify container username e.g. training, demo  
ENV VIRTUSER demo  
  
RUN apt-get update -qq  
RUN apt-get install -y build-essential checkinstall automake autoconf \  
pkg-config libtool libpcre3-dev libpcre3 libdumbnet1 \  
libdumbnet-dev libesmtp-dev libpcap-dev libgeoip-dev \  
libjson0 libjson0-dev libcurl4-openssl-dev  
RUN apt-get install -y git vim emacs nano tcpdump gawk rsyslog  
RUN apt-get install -y --no-install-recommends man-db  
RUN git clone https://github.com/rsyslog/libestr && cd libestr && \  
autoreconf -vfi && ./configure && make && make install && ldconfig  
RUN git clone https://github.com/rsyslog/liblognorm && cd liblognorm && \  
autoreconf -vfi && ./configure --disable-docs && make install && ldconfig  
RUN adduser --disabled-password --gecos "" $VIRTUSER  
RUN adduser --disabled-password --gecos "" \--home / --shell /usr/sbin/nologin
sagan  
RUN su -l -c 'git clone https://github.com/beave/sagan' $VIRTUSER  
RUN su -l -c 'cd sagan && ./configure --enable-geoip --enable-esmtp --enable-
libpcap && make' $VIRTUSER  
RUN git clone https://github.com/beave/sagan-rules /usr/local/etc/sagan-rules  
RUN cd /home/$VIRTUSER/sagan && make install  
RUN chown -R sagan:sagan /var/log/sagan /var/run/sagan  
RUN chown -R demo:sagan /usr/local/etc/  
RUN mkfifo /var/run/sagan.fifo  
RUN chown sagan:sagan /var/run/sagan.fifo  
RUN chmod 666 /var/run/sagan.fifo /var/log/*  
RUN chmod ugo+x /var/log/sagan  
RUN /bin/echo -e '#Sagan template\n$template sagan,"%fromhost-
ip%|%syslogfacility-text%|%syslogpriority-text%|%syslogseverity-
text%|%syslogtag%|%timegenerated:1:10:date-rfc3339%|%timegenerated:12:19:date-
rfc3339%|%programname%|%msg%\\\n"\n*.* |/var/run/sagan.fifo;sagan' >
/etc/rsyslog.d/sagan.conf  
RUN /bin/echo -e "$VIRTUSER ALL=(root)
NOPASSWD:/usr/local/sbin/sagan\n$VIRTUSER ALL=(root)
NOPASSWD:/usr/sbin/service rsyslog*" > /etc/sudoers.d/sagan  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/local/sbin/sagan  
RUN echo "export TMOUT=1800; readonly TMOUT" > /etc/profile.d/timeout.sh &&
chmod 555 /etc/profile.d/timeout.sh  

