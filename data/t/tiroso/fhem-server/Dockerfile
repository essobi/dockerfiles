FROM debian:stretch  
  
MAINTAINER Tim Sobisch  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
  
RUN touch /sbin/init \  
&& apt-get update \  
&& apt-get -y install \  
apt-utils \  
procps \  
wget \  
gnupg \  
build-essential \  
dfu-programmer \  
etherwake \  
snmp \  
snmpd \  
usbutils \  
apt-transport-https \  
telnet \  
sqlite3 \  
libdbi-perl \  
libdbd-sqlite3-perl \  
cpanminus \  
libwww-perl\  
libsoap-lite-perl \  
libxml-parser-perl \  
&& cpanm Net::WebSocket::Server \  
&& cpanm JSON \  
&& wget -qO - https://debian.fhem.de/archive.key | apt-key add \- \  
&& echo "deb http://debian.fhem.de/nightly/ /" | tee -a
/etc/apt/sources.list.d/fhem.list \  
&& apt-get update \  
&& apt-get -y install \  
fhem  
RUN pkill -f "fhem.pl" \  
&& update-rc.d -f fhem remove \  
&& userdel fhem \  
&& rm /opt/fhem/log/*.log \  
&& usermod -aG dialout root \  
&& chmod -R a+w /opt \  
&& chown -R root:dialout /opt \  
&& apt-get clean \  
&& apt-get autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR "/opt/fhem"  
#COPY start.sh File to Image  
COPY entrypoint.sh /entrypoint.sh  
# Create /opt/fhem/configDB.conf  
COPY configDB.conf /opt/fhem/configDB.conf  
# Create /opt/fhem/logDB.conf  
COPY logDB.conf /opt/fhem/logDB.conf  
  
RUN echo "pragma auto_vacuum=2;" | sqlite3 /opt/fhem/configDB.db \  
&& echo "CREATE TABLE 'history' (TIMESTAMP TIMESTAMP, DEVICE varchar(64), TYPE
varchar(64), EVENT varchar(512), READING varchar(64), VALUE varchar(128), UNIT
varchar(32));\  
CREATE TABLE 'current' (TIMESTAMP TIMESTAMP, DEVICE varchar(64), TYPE
varchar(64), EVENT varchar(512), READING varchar(64), VALUE varchar(128), UNIT
varchar(32));\  
CREATE INDEX Search_Idx ON 'history' (DEVICE, READING, TIMESTAMP);"\  
| sqlite3 /opt/fhem/log/logDB.db;  
  
#&& sed -i "1iattr global nofork 1" /opt/fhem/fhem.cfg \  
#RUN sed -i 's/updateInBackground.*$/updateInBackground 0\r\nattr global
nofork 1/' /opt/fhem/fhem.cfg \  
#RUN sed -i 's/attr global logfile.*$/attr global logfile -/'
/opt/fhem/fhem.cfg \  
RUN sed -i '/global nofork/d' /opt/fhem/fhem.cfg \  
&& sed -i "1iattr global nofork 1" /opt/fhem/fhem.cfg \  
&& echo '\ndefine InstallRoutine notify global:INITIALIZED sleep 1;;delete
InstallRoutine;;save;;configdb migrate;;sleep 1;;shutdown' >>
/opt/fhem/fhem.cfg \  
&& perl fhem.pl -d fhem.cfg | tee /opt/fhem/log/fhem_sqlite_install.log;  
  
RUN mkdir /opt/fhemorigin && mv /opt/fhem/* /opt/fhemorigin && rm
/opt/fhemorigin/log/*.log  
ENTRYPOINT ["bash","/entrypoint.sh"]  

