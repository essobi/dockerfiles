# calibre  
# docker run -d \  
# -v /media/books:/opt/calibre/library  
# -v /media/books:/opt/calibre/library  
# -p 8080:8080  
# markhuge/calibre  
FROM ubuntu:xenial  
  
ADD crontab /etc/cron.d/calibre-update  
  
RUN apt-get update -y \  
&& apt-get install -y calibre xvfb imagemagick\  
&& apt-get clean \  
&& rm -rf /var/cache/apt/* /var/lib/apt/lists/* \  
&& chmod 0644 /etc/cron.d/calibre-update  
  
EXPOSE 8080  
RUN mkdir -p /opt/calibre/{import,library}  
  
VOLUME ["/opt/calibre/library","/opt/calibre/import"]  
ENTRYPOINT ["/usr/bin/calibre-server", "--with-library=/opt/calibre/library"]  

