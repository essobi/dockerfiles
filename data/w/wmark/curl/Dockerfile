# just cURL  
#  
# I use this when cURL is not available or relies on a crippled TLS
implementation.  
FROM scratch  
MAINTAINER W. Mark Kubacki <wmark@hurrikane.de>  
ENTRYPOINT ["/usr/bin/curl"]  
  
# curl -fLRO http://ftp.de.debian.org/debian/pool/main/c/ca-certificates/ca-
certificates_20150426_all.deb  
# ar ca-certificates_20150426_all.deb && tar -xaf data.tar.xz  
# (inspect)  
#  
ADD ca-certificates.crt \  
/etc/ssl/certs/ca-certificates.crt  
ADD curl \  
/usr/bin/curl  

