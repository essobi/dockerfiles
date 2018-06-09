FROM debian:jessie  
MAINTAINER Joaquín de la Zerda, joaquindelazerda@gmail.com  
  
RUN apt-get update && apt-get install -y \  
libdbd-mysql-perl \  
libdbi-perl \  
libaio1 \  
libcurl3 \  
libev4 \  
libio-socket-ssl-perl \  
libnuma1 \  
libterm-readkey-perl \  
perl \  
rsync \  
wget \  
&& rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/info/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
ENV PERCONA_TOOLKIT_VERSION 2.2.18  
ENV PERCONA_XTRABACKUP_VERSION 2.4.4  
WORKDIR /tmp  
RUN wget https://www.percona.com/downloads/percona-
toolkit/${PERCONA_TOOLKIT_VERSION}/deb/percona-
toolkit_${PERCONA_TOOLKIT_VERSION}-1_all.deb && \  
dpkg -i percona-toolkit_${PERCONA_TOOLKIT_VERSION}-1_all.deb && \  
rm -f percona-toolkit_${PERCONA_TOOLKIT_VERSION}-1_all.deb  
  
RUN wget https://www.percona.com/downloads/XtraBackup/Percona-
XtraBackup-${PERCONA_XTRABACKUP_VERSION}/binary/debian/jessie/x86_64/percona-
xtrabackup-24_${PERCONA_XTRABACKUP_VERSION}-1.jessie_amd64.deb && \  
dpkg -i percona-xtrabackup-24_${PERCONA_XTRABACKUP_VERSION}-1.jessie_amd64.deb
&& \  
rm -f percona-xtrabackup-24_${PERCONA_XTRABACKUP_VERSION}-1.jessie_amd64.deb  
  
WORKDIR /  

