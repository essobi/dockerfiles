FROM alpine  
  
MAINTAINER Richard Arends  
  
VOLUME ["/data"]  
  
RUN apk update && \  
apk add perl make perl-image-exiftool libjpeg-turbo-utils && \  
wget -P /tmp ftp://download.gnu.org.ua/pub/release/renrot/renrot-1.2.0.tar.gz
&& \  
(cd /tmp/ ; tar xzf renrot-1.2.0.tar.gz) && \  
(cd /tmp/renrot-1.2.0 ; perl Makefile.PL PREFIX=/usr/local ; make ; make
install) && \  
sed -i -E 's/(^use diagnostics.*)/#\1/g' /usr/local/bin/renrot  
  
COPY rotate.sh /usr/local/bin/rotate.sh  
RUN chmod 755 /usr/local/bin/rotate.sh  
CMD ["/usr/local/bin/rotate.sh"]  
  

