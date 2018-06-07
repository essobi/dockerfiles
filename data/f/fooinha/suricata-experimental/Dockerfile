FROM fooinha/suricata-experimental:sid-build  
MAINTAINER fooinha <fooinha@gmail.com>  
ARG MAINTANER_NAME=fooinha  
ARG MAINTANER_EMAIL=fooinha@gmail.com  
  
# Build arguments  
ARG SURICATA_FEATURE=redis-async  
ARG SURICATA_DEBIAN_SID_VERSION=3.1.1-4ubuntu1  
ARG
SURICATA_DEBIAN_EXPERIMENTAL_VERSION=3.2.1-1+experimental~${SURICATA_FEATURE}  
ARG SURICATA_GIT_REPO=https://github.com/fooinha/suricata.git  
ARG SURICATA_GIT_BRANCH=dev-eve-output-redis-async-v4  
ARG SURICATA_DEBIAN_CHANGELOG_ENTRY="Experimental version of suricata 3.2.1
with async redis"  
ARG EXTRA_DEV_PACKAGES="libevent-dev"  
# Update  
RUN DEBIAN_FRONTEND=noninteractive apt-get update || true  
  
# Install build dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --fix-missing \  
${EXTRA_DEV_PACKAGES}  
  
WORKDIR /root  
  
# Clone source from git repository  
RUN git clone -v -b ${SURICATA_GIT_BRANCH} \--single-branch
${SURICATA_GIT_REPO}  
RUN cd suricata ; git checkout ${SURICATA_GIT_BRANCH}  
RUN mv suricata suricata-${SURICATA_DEBIAN_EXPERIMENTAL_VERSION}  
RUN tar cf suricata-${SURICATA_DEBIAN_EXPERIMENTAL_VERSION}.tar
suricata-${SURICATA_DEBIAN_EXPERIMENTAL_VERSION}/  
RUN gzip suricata-${SURICATA_DEBIAN_EXPERIMENTAL_VERSION}.tar  
  
# Get debian package source  
RUN DEBIAN_FRONTEND=noninteractive apt-get source
suricata=$SURICATA_DEBIAN_SID_VERSION  
RUN xz -d suricata_${SURICATA_DEBIAN_SID_VERSION}.debian.tar.xz ; tar xvf
suricata_${SURICATA_DEBIAN_SID_VERSION}.debian.tar  
  
# Copy debian directory to build dir  
RUN mv debian suricata-${SURICATA_DEBIAN_EXPERIMENTAL_VERSION}/  
  
WORKDIR /root/suricata-${SURICATA_DEBIAN_EXPERIMENTAL_VERSION}/  
  
# Get libhtp from git  
RUN git clone -v https://github.com/OISF/libhtp  
  
# Changelog  
RUN DEBFULLNAME=${MAINTANER_NAME} DEBEMAIL=${MAINTANER_EMAIL} dch -v
${SURICATA_DEBIAN_EXPERIMENTAL_VERSION} -D unstable
"${SURICATA_DEBIAN_CHANGELOG_ENTRY}"  
  
# Build package  
RUN ./debian/rules binary  
  
RUN apt-get remove -y \  
devscripts \  
make \  
autoconf \  
automake \  
dh-autoreconf \  
libtool \  
libpcap-dev \  
libnet1-dev \  
libyaml-0-2 \  
libyaml-dev \  
zlib1g-dev \  
libcap-ng-dev \  
libpcre3-dbg \  
libpcre3-dev \  
libmagic-dev \  
libnetfilter-queue-dev \  
libnetfilter-queue1 \  
libnfnetlink-dev \  
libnetfilter-log-dev \  
libprelude-dev \  
libnfnetlink0 \  
libjansson-dev \  
libnss3-dev \  
libnspr4-dev \  
libgeoip-dev \  
libluajit-5.1-common \  
libluajit-5.1-dev \  
libhiredis-dev \  
valgrind-dbg \  
vim vim-common vim-runtime xxd  
  
RUN apt-get -y install oinkmaster  
  
RUN dpkg -i ../suricata_${SURICATA_DEBIAN_EXPERIMENTAL_VERSION}_amd64.deb ||
true  
  
RUN dpkg -i ../suricata-
oinkmaster_${SURICATA_DEBIAN_EXPERIMENTAL_VERSION}_all.deb || true  
  
RUN mkdir -p /packages/  
  
RUN mv ../*.deb /packages/.  
  
RUN apt-get -y -f install  
  
RUN apt-get -y autoremove  
  
RUN apt-get -y install supervisor psmisc procps  
  
RUN mkdir -p /var/log/suricata /var/log/supervisor  
  
RUN mkdir -p /var/run/suricata  
  
RUN /etc/cron.daily/suricata-oinkmaster-updater || true  
  
RUN rm -rf /root/* /var/lib/apt/lists/*  
  
WORKDIR /var/log/suricata  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]  

