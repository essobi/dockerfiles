FROM ubuntu:16.04  
MAINTAINER gitterdone  
  
RUN apt-get update -y && apt-get install -y calibre xvfb imagemagick rsyslog
inotify-tools && apt-get clean  
  
RUN rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*rack*.com* && rm -rf
/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_precise-security_*  
  
# Create directory for library  
RUN mkdir -p /opt/calibre/library  
VOLUME ["/opt/calibre/library"]  
  
EXPOSE 8080  
# start calibre server, watching for changes to the database  
COPY run.sh /run.sh  
RUN ["chmod","+x","/run.sh"]  
CMD ["sh", "-c", "/usr/bin/calibre-server --with-library=/opt/calibre/library
& /run.sh"]  

