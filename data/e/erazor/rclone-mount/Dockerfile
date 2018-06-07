FROM alpine  
MAINTAINER ErAzOr2k  
  
ENV Version="current"  
ENV Arch="amd64"  
ENV RemotePath="backend:"  
ENV ConfigDir="/config"  
ENV ConfigName="rclone.conf"  
ENV MountCommands="--allow-other --allow-non-empty"  
RUN apk --no-cache add ca-certificates fuse wget \  
&& cd /tmp \  
&& wget -q http://downloads.rclone.org/rclone-${Version}-linux-${Arch}.zip \  
&& unzip /tmp/rclone-${Version}-linux-${Arch}.zip \  
&& mv /tmp/rclone-*-linux-${Arch}/rclone /usr/bin \  
&& rm -r /tmp/rclone*  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
VOLUME ["/config"]  
  
CMD ["/start.sh"]  

