FROM debian:8  
MAINTAINER Lubos Rendek <web@linuxconfig.org>  
  
# Get all asterisk prerequsites  
RUN apt-get update  
RUN apt-get install -y build-essential openssl libxml2-dev libncurses5-dev
uuid-dev sqlite3 libsqlite3-dev pkg-config curl libjansson-dev  
  
# Download and decompress latest asterisk version  
RUN curl -s http://downloads.asterisk.org/pub/telephony/certified-
asterisk/certified-asterisk-13.1-current.tar.gz | tar xz  
  
# Asterisk compilation & installation  
WORKDIR /certified-asterisk-13.1-cert2  
RUN ./configure; make; make install; make samples  
  
CMD ["/usr/sbin/asterisk", "-vvvvvvv"]  
  

