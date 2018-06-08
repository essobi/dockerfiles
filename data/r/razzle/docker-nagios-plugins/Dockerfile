FROM razzle/docker-nagios-core:core-4.3.2  
MAINTAINER RazzDazz  
# Using instructions from  
# https://support.nagios.com/kb/article/nagios-core-installing-nagios-core-
from-source.html#Ubuntu  
ENV REFRESHED_AT 2017-06-30  
ENV DEBIAN_FRONTEND noninteractive  
  
#  
# Install nagios plugins  
#  
ENV NAGIOS_PLUGINS_TAR release-2.2.1.tar.gz  
ENV NAGIOS_PLUGINS_DIR nagios-plugins-release-2.2.1  
# Install missing packages  
RUN apt-get -yqq update && \  
apt-get -yqq upgrade && \  
apt-get -yqq install \  
bc \  
build-essential \  
dc \  
gawk \  
gettext \  
libmcrypt-dev \  
libnet-snmp-perl \  
libssl-dev \  
snmp && \  
rm -rf /var/lib/apt/lists/*  
  
# Download and extract nagios sourcen  
RUN mkdir -p /tmp/nagios-plugins && \  
cd /tmp/nagios-plugins/ && \  
wget -O nagios-plugins.tar.gz https://github.com/nagios-plugins/nagios-
plugins/archive/${NAGIOS_PLUGINS_TAR} && \  
tar zxvf nagios-plugins.tar.gz && \  
rm -f nagios-plugins.tar.gz  
  
# wget --no-check-certificate -O nagios-plugins.tar.gz
https://github.com/nagios-plugins/nagios-plugins/archive/release-2.2.1.tar.gz  
# Compile  
RUN cd /tmp/nagios-plugins/${NAGIOS_PLUGINS_DIR}/ && \  
./tools/setup && \  
./configure && \  
make all && \  
make install && \  
rm -dfr /tmp/nagios-plugins/  
  
# run nagios  
CMD ["/tmp/docker-entrypoint.sh"]  

