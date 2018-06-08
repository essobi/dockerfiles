FROM postgres:9.2  
MAINTAINER Guillaume Hain <zedtux@zedroot.org>  
  
ENV SWIFT_OS_AUTH_URL 'https://auth.cloud.ovh.net/v2.0'  
ADD pg2swift-start pg2swift-backup-job pg2swift-restore-job pg2swift-build-
swift-env /usr/local/bin/  
  
RUN apt-get update && \  
apt-get install -y python-swiftclient cron && \  
rm -rf /var/lib/apt/lists/* && \  
sed -i '/pam_loginuid.so/ s/^/#/' /etc/pam.d/cron && \  
chmod +x /usr/local/bin/pg2swift-start \  
/usr/local/bin/pg2swift-backup-job \  
/usr/local/bin/pg2swift-restore-job \  
/usr/local/bin/pg2swift-build-swift-env  
  
ENTRYPOINT ["pg2swift-start"]  

