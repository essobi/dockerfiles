FROM fedora  
  
RUN mkdir -p /opt/calibre/; yum update -y; yum install -y calibre; yum -y
clean all  
VOLUME ["/opt/calibre"]  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/calibre-server", "--with-library=/opt/calibre"]  

