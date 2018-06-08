FROM busybox  
  
MAINTAINER foster63@gmail.com  
  
RUN wget http://downloads.rclone.org/rclone-current-linux-amd64.zip \  
&& unzip rclone-current-linux-amd64.zip \  
&& cp ./rclone-v*-linux-amd64/rclone /usr/sbin \  
&& chown root:root /usr/sbin/rclone && chmod 755 /usr/sbin/rclone  
  
VOLUME ["/config"]  
  
ENTRYPOINT ["/usr/sbin/rclone", "--config", "/config/.rclone.conf"]  
  
CMD ["--version"]  

