FROM bitnami/minideb  
  
RUN apt-get update && \  
apt-get install -y ca-certificates wget unzip && \  
wget https://downloads.rclone.org/rclone-current-linux-amd64.zip && \  
unzip rclone-current-linux-amd64.zip && \  
cd rclone-*-linux-amd64 && \  
cp rclone /usr/bin/ && \  
chmod 755 /usr/bin/rclone && \  
rm -R /rclone* && \  
rclone --version  

