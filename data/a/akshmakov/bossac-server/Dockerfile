FROM akshmakov/bossa  
  
#socat  
RUN apt-get update -y && apt-get install -y socat tftpd-hpa && rm -rf
/var/lib/apt/lists/*  
  
ENV SERVER_BINS_DIR /srv/tftp  
  
COPY bossac-server.sh /usr/local/bin/bossac-server  
  
EXPOSE 69  
ENTRYPOINT [ "bossac-server" ]  
  

