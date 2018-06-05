FROM mongo:3.4  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y unzip && \  
apt-get clean  
  
ADD https://downloads.rclone.org/rclone-current-linux-amd64.zip
/tmp/rclone.zip  
  
RUN cd /tmp && \  
unzip /tmp/rclone.zip && \  
cp /tmp/rclone-*-linux-amd64/rclone /usr/bin && \  
chmod +x /usr/bin/rclone && \  
rm -rf /tmp/rclone*  
  
ENTRYPOINT ["/opt/run-backups"]  
  
VOLUME ["/backups"]  
  
ENV HOST=localhost \  
PREFIX=mongodb \  
INTERVAL=86400 \  
RCLONE_CONFIG=/run/secrets/rclone.conf \  
RCLONE_LOCAL_KEEP=1w \  
RCLONE_REMOTE_KEEP=2w  
  
ADD run-backups /opt/  

