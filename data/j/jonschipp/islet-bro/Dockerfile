# Bro  
#  
# VERSION 1.1  
FROM ubuntu  
MAINTAINER Jon Schipp <jonschipp@gmail.com>  
  
# Specify container username e.g. training, demo  
ENV VIRTUSER demo  
# Specify Bro version to download and install (e.g. bro-2.2, bro-2.3)  
ENV BRO_VERSION bro-2.3.2  
# Place to install bro  
ENV DST /home/$VIRTUSER/bro  
  
RUN apt-get update -qq  
RUN apt-get install -y build-essential cmake make gcc g++ flex bison libpcap-
dev libgeoip-dev libssl-dev python-dev zlib1g-dev libmagic-dev swig2.0 wget  
RUN apt-get install -y git gawk vim emacs nano tcpdump rsyslog  
RUN apt-get install -y --no-install-recommends man-db  
RUN adduser --disabled-password --gecos "" $VIRTUSER  
RUN su -l -c "wget http://www.bro.org/downloads/release/$BRO_VERSION.tar.gz &&
tar -xzf $BRO_VERSION.tar.gz" $VIRTUSER  
RUN su -l -c "cd $BRO_VERSION && ./configure --prefix=$DST && make && make
install" $VIRTUSER  
RUN rm -rf /home/$VIRTUSER/$BRO_VERSION*  
RUN echo "PATH=$PATH:/usr/local/bro/bin/" > /etc/profile.d/bro.sh  
RUN echo "export BRO_DNS_FAKE=1" >> /etc/profile.d/bro.sh && chmod 555
/etc/profile.d/bro.sh  
RUN echo "export TMOUT=1800; readonly TMOUT" > /etc/profile.d/timeout.sh &&
chmod 555 /etc/profile.d/timeout.sh  
RUN su -l -c 'ln -s /exercises exercises' $VIRTUSER  
RUN ln -s $DST /usr/local/bro  
RUN setcap cap_net_raw,cap_net_admin=eip $DST/bin/bro  

