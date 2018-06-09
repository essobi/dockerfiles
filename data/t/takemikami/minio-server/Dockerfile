FROM base/archlinux  
  
RUN pacman -Syy && pacman -S --noconfirm wget  
  
RUN mkdir /opt/minio-server \  
&& cd /opt/minio-server \  
&& wget https://dl.minio.io:9000/updates/2015/Jun/linux-amd64/minio \  
&& chmod +x /opt/minio-server/minio \  
&& mkdir /var/minio-server  
  
ADD minio-server /usr/local/bin/  
RUN chmod +x /usr/local/bin/minio-server  
  
CMD ["/usr/local/bin/minio-server"]  

