FROM shift/ubuntu:15.04  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
WORKDIR /opt  
  
RUN apt-get update \  
&& apt-get upgrade --yes --force-yes \  
&& apt-get \--yes --force-yes install libpcre3 libpcre3-dbg libpcre3-dev \  
build-essential autoconf automake libtool libpcap-dev libnet1-dev \  
libyaml-0-2 libyaml-dev zlib1g zlib1g-dev make flex bison libmagic-dev \  
libjansson-dev libjansson4 libnss3-dev libnspr4-dev libgeoip1 libgeoip-dev \  
libnetfilter-queue-dev libnetfilter-queue1 libnfnetlink-dev \  
libnfnetlink0 libcap-ng0 libcap-ng-dev oinkmaster ethtool curl cron \  
python-simplejson libluajit-5.1-dev luajit ulogd2 libprelude2 psmisc \  
&& curl -O http://www.openinfosecfoundation.org/download/suricata-2.0.8.tar.gz
\  
&& tar xfvz suricata-2.0.8.tar.gz \  
&& cd suricata-2.0.8 \  
&& ./configure --prefix=/usr/ --sysconfdir=/etc/ --localstatedir=/var/ \  
\--disable-gccmarch-native --with-libnss-libraries=/usr/lib \  
\--with-libnss-includes=/usr/include/nss/ --enable-nfqueue \  
\--with-libcap_ng-libraries=/usr/local/lib --with-libcap_ng-
includes=/usr/local/include \  
\--with-libnspr-libraries=/usr/lib \  
\--with-libnspr-includes=/usr/include/nspr \  
\--with-nflog \  
\--with-libluajit \  
&& make clean \  
&& make \  
&& make install-full \  
&& ldconfig \  
&& apt-get purge --yes --force-yes \  
autoconf automake autotools-dev binutils bison build-essential bzip2 cpp \  
cpp-4.9 dpkg-dev fakeroot flex g++ g++-4.9 gcc gcc-4.9 \  
libbison-dev libc-dev-bin libc6-dev \  
libcap-ng-dev libcilkrts5 libcloog-isl4 \  
libfakeroot \  
libfl-dev libgcc-4.9-dev libgeoip-dev libjansson-dev \  
libjs-jquery \  
libltdl-dev libluajit-5.1-2 libluajit-5.1-common libluajit-5.1-dev \  
libmagic-dev libnet1-dev \  
libnetfilter-queue-dev libnfnetlink-dev libnspr4-dev libnss3-dev \  
libpcap-dev \  
libpcap0.8-dev libpcre3-dev libpcrecpp0 \  
libpython-stdlib libpython2.7-minimal \  
libsoftware-license-perl libstdc++-4.9-dev libsub-exporter-perl \  
libyaml-dev linux-libc-dev m4 make \  
manpages manpages-dev patch perl perl-modules pkg-config psmisc \  
python python-minimal python-simplejson python2.7 python2.7-minimal \  
rename zlib1g-dev \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& rm -rf /opt/suricata-2.0.8 /opt/suricata-2.0.8.tar.gz  
  
VOLUME /etc/suricata  
VOLUME /etc/suricata/rules  
VOLUME /var/log/suricata  
  
ADD files/oinkmaster.conf /etc/oinkmaster.conf  
ADD files/blacklist.sh /blacklists.sh  
ADD files/start.sh /start.sh  
RUN chmod u+x /start.sh /blacklists.sh  
ENTRYPOINT ["/start.sh"]  
  

