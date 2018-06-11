# Usage:  
# docker run -it --rm -v ~/sync/keepass2.kdbx:/DB.kdbx:ro \  
# --name kpcli-search kpcli-search <search term>  
FROM debian:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
perl libcrypt-rijndael-perl libsort-naturally-perl \  
libterm-readkey-perl libterm-shellui-perl libfile-keepass-perl \  
libclone-perl libterm-readline-gnu-perl curl && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD kpcli-3.1-modified.pl /usr/bin/kpcli-3.1-modified.pl  
RUN chmod 755 /usr/bin/kpcli-3.1-modified.pl  
  
ENTRYPOINT ["kpcli-3.1-modified.pl", "-kdb", "/DB.kdbx", "-s"]  

