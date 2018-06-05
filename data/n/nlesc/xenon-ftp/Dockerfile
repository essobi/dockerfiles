FROM nlesc/xenon-phusion-base  
MAINTAINER Stefan Verhoeven "s.verhoeven@esciencecenter.nl"  
# update packages and install FTP daemon program 'vsftpd'  
RUN apt-get update && \  
apt-get install -y vsftpd && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
  
# configure the vsftpd service to start automatically with the container  
mkdir /etc/service/vsftpd && \  
echo "#!/bin/sh" > /etc/service/vsftpd/run && \  
echo "/usr/sbin/vsftpd /etc/vsftpd.conf" >> /etc/service/vsftpd/run && \  
chmod +x /etc/service/vsftpd/run && \  
mkdir -p /var/run/vsftpd/empty && \  
  
# copy fixtures also for anonymous user (/srv/ftp)  
# Xenon's filesystem integration tests expect certain directory structure,
create it here:  
cd /srv/ftp/ && \  
mkdir -p filesystem-test-fixture/links && \  
echo "Hello World" > filesystem-test-fixture/links/file0 && \  
touch filesystem-test-fixture/links/file1 && \  
ln -s /srv/ftp/filesystem-test-fixture/links/file0 /srv/ftp/filesystem-test-
fixture/links/link0 && \  
ln -s /srv/ftp/filesystem-test-fixture/links/file1 /srv/ftp/filesystem-test-
fixture/links/link1 && \  
ln -s /srv/ftp/filesystem-test-fixture/links/file2 /srv/ftp/filesystem-test-
fixture/links/link2 && \  
ln -s /srv/ftp/filesystem-test-fixture/links/link0 /srv/ftp/filesystem-test-
fixture/links/link3 && \  
ln -s /srv/ftp/filesystem-test-fixture/links/link2 /srv/ftp/filesystem-test-
fixture/links/link4 && \  
ln -s /srv/ftp/filesystem-test-fixture/links/link6 /srv/ftp/filesystem-test-
fixture/links/link5 && \  
ln -s /srv/ftp/filesystem-test-fixture/links/link5 /srv/ftp/filesystem-test-
fixture/links/link6 && \  
chown -R ftp.ftp /srv/ftp/filesystem-test-fixture && \  
cd /home/xenon  
# COPY vsftpd configuration from Docker context to inside the container  
ADD vsftpd.conf /etc/vsftpd.conf  
  
EXPOSE 21  
EXPOSE 3000-3100  
  
HEALTHCHECK \--interval=1s CMD curl -f ftp://localhost/ || exit 1  

