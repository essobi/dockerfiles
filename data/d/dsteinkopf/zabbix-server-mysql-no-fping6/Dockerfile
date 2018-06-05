FROM zabbix/zabbix-server-mysql:ubuntu-latest  
  
MAINTAINER Dirk Steinkopf "https://github.com/dsteinkopf"  
  
RUN mv /usr/bin/fping6 /usr/bin/fping6.hide  
  
# enable the multiverse  
RUN echo 'deb http://archive.ubuntu.com/ubuntu/ trusty multiverse' >>
/etc/apt/sources.list && \  
echo 'deb http://archive.ubuntu.com/ubuntu/ trusty-updates multiverse' >>
/etc/apt/sources.list && \  
echo 'deb http://archive.ubuntu.com/ubuntu/ trusty-security multiverse' >>
/etc/apt/sources.list  
  
# bc is for some externalscripts (e.g. zext_ssl_cert.sh)  
  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y autoremove && \  
apt-get clean && \  
apt-get install -y \  
bc \  
python-pip \  
python-requests \  
snmp \  
snmp-mibs-downloader  
  
# seems important for mib lookup to work:  
ENV
MIBDIRS=/usr/share/snmp/mibs:/var/lib/zabbix/mibs:/usr/share/mibs/ietf:/usr/share/mibs/iana  
# enable snmp mibs loading:  
# remove problematic mibs which result in errors and are not needed (...why is
this necessary?...)  
RUN sed -i 's/^\\( *mibs *:.*\\)$/# \1/g' /etc/snmp/snmp.conf && \  
rm /usr/share/mibs/iana/IANA-IPPM-METRICS-REGISTRY-MIB && \  
rm /usr/share/mibs/ietf/SNMPv2-PDU && \  
rm /usr/share/mibs/ietf/IPATM-IPMC-MIB && \  
snmptranslate .iso.3.6.1.6.3.1.1.5.3  
  
RUN pip install requests  
  

