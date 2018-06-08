FROM ubuntu:14.04  
MAINTAINER nekoya "ryo.studiom@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "Asia/Tokyo\n" > /etc/timezone  
RUN /usr/sbin/dpkg-reconfigure -f noninteractive tzdata  
  
RUN sed -i 's/archive.ubuntu.com/ftp.jaist.ac.jp\/pub\/Linux/'
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y \  
build-essential \  
cpanminus \  
git \  
libmysqlclient18 \  
libmysqlclient-dev \  
libcapture-tiny-perl \  
libnet-snmp-perl \  
librrds-perl \  
libsnmp-perl \  
patch \  
smistrip \  
snmp \  
wget  
  
# SNMP  
RUN wget http://security.ubuntu.com/ubuntu/pool/multiverse/s/snmp-mibs-
downloader/snmp-mibs-downloader_1.1_all.deb  
RUN dpkg -i snmp-mibs-downloader_1.1_all.deb  
RUN rm /etc/snmp/snmp.conf  
  
# Install CloudForecast  
WORKDIR /var/lib  
RUN git clone https://github.com/kazeburo/cloudforecast.git  
WORKDIR /var/lib/cloudforecast  
RUN cpanm -l extlib --installdeps .  
RUN cpanm -l extlib DBD::mysql  
  
# avoid Perl's Gearman::Client broken test  
RUN apt-get install -y gearman-job-server  
  
# create data dir  
RUN mkdir data  
  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 5000  
CMD ["/start.sh"]  

