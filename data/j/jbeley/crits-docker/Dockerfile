FROM ubuntu:16.04  
MAINTAINER jdb  
  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
  
  
  
USER root  
RUN apt-get -qq update && \  
apt-get install -y software-properties-common && \  
apt-get -qq update && apt-get install -y --fix-missing && \  
apt-get -y -q dist-upgrade && \  
apt-get install -y -q \  
apache2 \  
build-essential \  
curl \  
git \  
libevent-dev \  
libz-dev \  
libfuzzy-dev \  
libjpeg-dev \  
libldap2-dev \  
libpcap-dev \  
libpcre3-dev \  
libsasl2-dev \  
libssl-dev \  
libtool \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
numactl \  
p7zip-full \  
python-dev \  
python-pip \  
ssdeep \  
swig \  
supervisor \  
upx \  
vim-tiny \  
wget \  
zip \  
libapache2-mod-wsgi \  
build-essential \  
rsyslog \  
logrotate \  
sudo \  
autoconf \  
libjansson-dev \  
libmagic-dev \  
flex \  
bison \  
libimage-exiftool-perl \  
poppler-utils \  
wireshark \  
antiword  
  
  
  
  
  
WORKDIR /etc/logrotate.d  
RUN echo "/data/crits/logs/crits.log {" > crits ; \  
echo " rotate 30" >> crits ; \  
echo " dateext" >> crits ; \  
echo " missingok" >> crits ; \  
echo " notifempty" >> crits ; \  
echo " compress" >> crits ; \  
echo " weekly" >> crits ; \  
echo " copytruncate" >> crits ; \  
echo "}" >> crits  
  
RUN git clone https://github.com/crits/crits/ /data/crits/  
RUN git clone https://github.com/crits/crits_services/
/data/crits_services.unused/  
#ADD ./crits /data/crits/  
#ADD ./crits_services /data/crits_services.unused/  
  
COPY crontab /tmp  
RUN cat /tmp/crontab | crontab  
COPY supervisord.conf /etc/supervisor/conf.d/crits.conf  
  
  
RUN LDFLAGS=-L/usr/local/lib \  
CFLAGS=-I/usr/local/include \  
SWIG_FEATURES="-cpperraswarn -includeall -I/usr/local/include" \  
pip install M2Crypto \  
pycrypto \  
qrcode && \  
pip install -r /data/crits/requirements.txt  
  
WORKDIR /tmp  
RUN openssl req -nodes -newkey rsa:4096 -keyout new.cert.key -out new.cert.csr
-subj "/CN=CRITs/O=DFIR/C=US" && \  
openssl x509 -in new.cert.csr -out new.cert.cert -req -signkey new.cert.key
-days 1825 && \  
cp new.cert.cert /etc/ssl/certs/crits.crt &&\  
cp new.cert.key /etc/ssl/private/crits.plain.key  
  
  
  
ENV YARA_VERSION 3.6.1  
RUN cd /tmp/ && \  
git clone --recursive --branch v$YARA_VERSION
https://github.com/VirusTotal/yara.git && \  
cd /tmp/yara && \  
./bootstrap.sh && \  
sync && \  
./configure --enable-magic --enable-dotnet --prefix=/usr && \  
make clean all install && \  
pip install --upgrade yara-python  
  
  
  
  
  
#RUN ldconfig && \  
# apt-get remove -qq -y --purge build-essential libtool && \  
# apt-get autoremove -qq -y --purge && \  
# apt-get clean -qq -y && \  
# rm -rf /tmp/* && \  
# rm -rf /var/lib/apt/lists/*  
  
  
ADD firstboot.sh /firstboot.sh  
RUN touch /firstboot.tmp  
EXPOSE 443  
  
  
ENTRYPOINT /usr/bin/supervisord -c /etc/supervisor/supervisord.conf  

