FROM phusion/baseimage:0.10.0  
MAINTAINER Julian Haupt <jh@coinctrl.com>  
  
RUN apt-get update -qq && \  
apt-get install -y wget build-essential libssl-dev libboost-all-dev libdb-dev
libtool libdb5.3 libdb5.3-dev libdb5.3++-dev \  
git ntp make g++ gcc autoconf cpp ngrep iftop sysstat autotools-dev pkg-config
\  
libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools
libprotobuf-dev protobuf-compiler libqrencode-dev && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ENV TERM xterm  
  
ENV UNITCURRENCY_VERSION 1.0.2.1  
ENV UNITCURRENCY_USER_ID 1000  
ENV UNITCURRENCY_USER unitcurrency  
  
ENV UNITCURRENCY_GROUP_ID 1000  
ENV UNITCURRENCY_GROUP unitcurrency  
  
ENV UNITCURRENCY_HOME /var/lib/unitcurrency  
ENV UNIVERSALCURRENCYD_PARAMS ""  
RUN groupadd -g ${UNITCURRENCY_GROUP_ID} ${UNITCURRENCY_GROUP} && \  
useradd -u ${UNITCURRENCY_USER_ID} -g ${UNITCURRENCY_GROUP} -s /bin/false -m
-d ${UNITCURRENCY_HOME} ${UNITCURRENCY_USER}  
  
RUN cd /tmp && \  
wget -q http://miniupnp.free.fr/files/download.php?file=miniupnpc-2.0.tar.gz
-O miniupnpc-2.0.tar.gz && \  
tar xzf miniupnpc-2.0.tar.gz && \  
cd miniupnpc-2.0 && \  
make install && \  
cd .. && \  
rm -rf miniupnpc-2.0 miniupnpc-2.0.tar.gz  
  
RUN curl -L --silent -o /tmp/unitcurrency.tar.gz
https://github.com/unitcurrency/unitcurrency/archive/${UNITCURRENCY_VERSION}.tar.gz
&& \  
tar -xvzf /tmp/unitcurrency.tar.gz -C /usr/src && \  
rm /tmp/unitcurrency.tar.gz && \  
cd /usr/src/unitcurrency-${UNITCURRENCY_VERSION}/src/leveldb && \  
chmod 755 build_detect_platform && \  
make libleveldb.a libmemenv.a && \  
cd .. && \  
make -f makefile.unix && \  
cp /usr/src/unitcurrency-${UNITCURRENCY_VERSION}/src/UniversalCurrencyd
/usr/local/bin/ && \  
rm -r /usr/src/unitcurrency-${UNITCURRENCY_VERSION}  
  
VOLUME ["${UNITCURRENCY_HOME}"]  
  
ADD etc/ /etc/  
ADD docker-entrypoint.sh /usr/local/sbin/docker-entrypoint.sh  
  
ENTRYPOINT ["/usr/local/sbin/docker-entrypoint.sh"]  
  
EXPOSE 14158 14157  
# phusion/baseimage docker optimized init script  
CMD ["/sbin/my_init"]  

