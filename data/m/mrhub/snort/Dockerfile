#sudo docker build -t="myproject/snort:1.0" .  
# eieie  
FROM ubuntu:14.04  
MAINTAINER Opart Moxes  
# Install Requirements  
RUN apt-get update && \  
apt-get install -y curl && \  
/bin/bash -c "$(curl -sL https://git.io/vokNn)" && \  
apt-fast update && \  
apt-fast install -y build-essential libpcap-dev libpcre3-dev libdumbnet-dev \  
bison flex zlib1g-dev nano wget git libmysqlclient-dev mysql-client autoconf
libtool \  
libcrypt-ssleay-perl liblwp-useragent-determined-perl  
  
# Install DAQ 2.0.6 and install snort 2.9.9.0  
RUN mkdir /root/snort_src && \  
cd /root/snort_src/ && \  
wget https://www.snort.org/downloads/snort/daq-2.0.6.tar.gz && \  
wget https://www.snort.org/downloads/snort/snort-2.9.9.0.tar.gz && \  
tar -xvzf daq-2.0.6.tar.gz && \  
tar -xvzf snort-2.9.9.0.tar.gz && \  
cd /root/snort_src/daq-2.0.6 && \  
./configure && make -j3 && \  
make install && \  
cd /root/snort_src/snort-2.9.9.0 && \  
./configure --enable-sourcefire && \  
make -j3 && sudo make install && \  
cd /root/snort_src && \  
ldconfig && \  
ln -s /usr/local/bin/snort /usr/sbin/snort && \  
groupadd snort && \  
useradd snort -r -s /sbin/nologin -c SNORT_IDS -g snort && \  
mkdir /etc/snort && \  
mkdir /etc/snort/rules && \  
mkdir /etc/snort/rules/iplists && \  
mkdir /etc/snort/preproc_rules && \  
mkdir /usr/local/lib/snort_dynamicrules && \  
mkdir /etc/snort/so_rules && \  
touch /etc/snort/rules/iplists/default.blacklist && \  
touch /etc/snort/rules/iplists/default.whitelist && \  
touch /etc/snort/rules/local.rules && \  
mkdir /var/log/snort && \  
mkdir /var/log/snort/archived_logs && \  
chmod -R 5775 /etc/snort && \  
chmod -R 5775 /var/log/snort && \  
chmod -R 5775 /var/log/snort/archived_logs && \  
chmod -R 5775 /etc/snort/so_rules && \  
chmod -R 5775 /usr/local/lib/snort_dynamicrules && \  
chown -R snort:snort /etc/snort && \  
chown -R snort:snort /var/log/snort && \  
chown -R snort:snort /usr/local/lib/snort_dynamicrules && \  
cd /root/snort_src/snort-2.9.9.0/etc/ && \  
cp *.conf* /etc/snort && \  
cp *.map /etc/snort && \  
cp *.dtd /etc/snort && \  
cd /root/snort_src/snort-2.9.9.0/src/dynamic-
preprocessors/build/usr/local/lib/snort_dynamicpreprocessor/ && \  
cp * /usr/local/lib/snort_dynamicpreprocessor/ && \  
cp /etc/snort/snort.conf /etc/snort/snort.conf.bak && \  
cp /etc/snort/snort.conf.bak /etc/snort/snort.conf  
  
# Start Barnyard2 Install  
RUN cd /root/snort_src && \  
wget https://github.com/firnsy/barnyard2/archive/v2-1.13.tar.gz -O
barnyard2-2-1.13.tar.gz && \  
tar zxvf barnyard2-2-1.13.tar.gz && \  
cd /root/snort_src/barnyard2-2-1.13 && \  
autoreconf -fvi -I ./m4 && \  
./configure --with-mysql --with-mysql-libraries=/usr/lib/x86_64-linux-gnu && \  
make -j3 && \  
make install && \  
ln -s /usr/include/dumbnet.h /usr/include/dnet.h && \  
ldconfig && \  
cp etc/barnyard2.conf /etc/snort && \  
mkdir /var/log/barnyard2 && \  
chown snort.snort /var/log/barnyard2 && \  
touch /var/log/snort/barnyard2.waldo && \  
chown snort.snort /var/log/snort/barnyard2.waldo && \  
touch /etc/snort/sid-msg.map  
  
# Coppy config files  
COPY config /root/config  
RUN cp /root/config/snort.conf /etc/snort/snort.conf && \  
cp /root/config/barnyard2.conf /etc/snort/barnyard2.conf && \  
cp /root/config/rules/local.rules /etc/snort/rules/local.rules && \  
cp /root/config/rules/sid-msg.map /etc/snort/sid-msg.map && \  
chmod o-r /etc/snort/barnyard2.conf && \  
snort -T -c /etc/snort/snort.conf  
WORKDIR /root  
#ADD /config/run.sh /root/run.sh  
#RUN sudo chmod +x /root/run.sh  
#CMD ["/bin/sh", "-l", "-c", "/root/run.sh"]  

