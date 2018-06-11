FROM mongo:3.2  
ENV RCLONE_VERSION="v1.39"  
ENV PLATFORM_ARCH="amd64"  
RUN apt-get update -y && apt-get install -y curl vim unzip && \  
curl
https://downloads.rclone.org/${RCLONE_VERSION}/rclone-${RCLONE_VERSION}-linux-${PLATFORM_ARCH}.zip
-o /tmp/rclone.zip && \  
unzip /tmp/rclone.zip -d /tmp && \  
mv /tmp/rclone*/rclone /usr/bin &&\  
rm -rf /tmp/* /var/lib/apt/lists/*  
  
COPY scripts/backup.sh /usr/local/bin/backup.sh  
COPY scripts/init-mongo.sh /usr/local/bin/init-mongo.sh  
COPY scripts/restore.sh /usr/local/bin/restore.sh  

