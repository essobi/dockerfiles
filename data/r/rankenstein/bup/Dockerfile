FROM debian:7  
MAINTAINER Candid Dauth <cdauth@cdauth.eu>  
  
RUN apt-get update && apt-get install -y \  
bup \  
curlftpfs \  
encfs  
  
COPY ./backup.sh /usr/local/bin/backup.sh  
  
VOLUME [ "/backup" ]  
  
CMD "backup.sh"

