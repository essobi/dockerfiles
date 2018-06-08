# dependencies and scripts to run  
# https://personaltelco.net/wiki/FooCabFirmwareHowTo  
FROM debian:stable  
MAINTAINER ptp-ops@googlegroups.com  
  
ENV IMAGE personaltelco/node-builder  
  
# Install Debian main packages  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
build-essential ca-certificates cpanminus file flex gawk gcc-multilib git \  
libncurses5-dev libnet-ssleay-perl libcrypt-ssleay-perl libssl-dev \  
openssl python rsync subversion unzip wget zlib1g-dev \  
&& apt-get clean  
  
# Install modules from CPAN  
RUN cpanm --skip-satisfied \  
NetAddr::IP::Lite Getopt::Long JSON LWP::Simple LWP::Protocol::https  
  
# Fetch source trees  
WORKDIR /src  
RUN git clone git://github.com/personaltelco/ptp-openwrt-files.git  
RUN git clone git://git.lede-project.org/source.git lede  
  
# Update and install LEDE package feeds  
WORKDIR /src/lede  
ADD config/openwrt/feeds.conf feeds.conf  
RUN scripts/feeds update -a  
RUN scripts/feeds install -a  
  
# Ready to build  
WORKDIR /src  
ADD ./bin /opt/bin  
ENTRYPOINT ["/opt/bin/build.sh"]  

