FROM aguamala/centos:7  
MAINTAINER "gabo" <aguamala@deobieta.com>  
RUN yum -y install lsyncd  
  
ENV RCLONE_VERSION 1.28  
ADD "http://downloads.rclone.org/rclone-v${RCLONE_VERSION}-linux-amd64.zip"
"/"  
  
RUN unzip rclone-v${RCLONE_VERSION}-linux-amd64.zip && \  
mv rclone-v${RCLONE_VERSION}-linux-amd64/rclone /usr/local/bin/rclone &&\  
rm -rf /rclone-v${RCLONE_VERSION}-linux-amd64.zip && \  
rm -rf /rclone-v${RCLONE_VERSION}-linux-amd64  
  
COPY lsyncd-backup.conf /lsyncd-backup.conf  
COPY lsyncd-sync.conf /lsyncd-sync.conf  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["lsyncd","/lsyncd.conf"]  

