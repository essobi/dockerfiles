FROM golang  
  
ENV DBXCLI_VERSION v2.1.0  
ADD
https://github.com/dropbox/dbxcli/releases/download/$DBXCLI_VERSION/dbxcli-
linux-amd64 /usr/local/bin/dbxcli  
RUN chmod +x /usr/local/bin/dbxcli  
  
COPY backup.sh /  
  
VOLUME /files  
VOLUME /etc/backup  
VOLUME /root/.config/dbxcli  
  
WORKDIR /files  
  
ENTRYPOINT ["/backup.sh"]  

