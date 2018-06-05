FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install build-essential curl -y  
  
ADD https://www.openssl.org/source/old/1.0.1/openssl-1.0.1f.tar.gz /builddir/  
RUN cd /builddir && curl -O
ftp://ftp.proftpd.org/distrib/source/proftpd-1.3.5b.tar.gz  
  
WORKDIR /builddir/  
RUN tar xf openssl-1.0.1f.tar.gz  
RUN tar xf proftpd-1.3.5b.tar.gz  
  
WORKDIR /builddir/openssl-1.0.1f  
RUN ./config && make && make install_sw  
  
WORKDIR /builddir/proftpd-1.3.5b  
RUN ./configure LDFLAGS="-Wl,--no-as-needed -ldl" \--prefix=/usr/local/ftpd
--with-modules=mod_tls --with-includes=/usr/local/ssl/include --with-
libraries=/usr/local/ssl/lib && make && make install  
  
RUN mkdir /workdir/  
WORKDIR /workdir  
RUN mkdir certs  
RUN /usr/local/ssl/bin/openssl req -x509 -newkey rsa:2048 -keyout
certs/key.pem -out certs/cert.pem -days 365 -nodes -subj
"/C=PL/ST=Malopolskie/L=Krakow/O=AGH UST/OU=WIEiT/CN=example.kacperzuk.pl"  
  
ADD proftpd.conf /usr/local/ftpd/etc/  
  
EXPOSE 21  
RUN useradd -s /bin/bash -d /workdir/testuser -m testuser && (echo
testuser:bordodeszato2009 | chpasswd)  
  
RUN touch /workdir/testuser/hello_world.txt && chown testuser:
/workdir/testuser/hello_world.txt  
  
CMD /usr/local/ftpd/sbin/proftpd --nodaemon -d 6  

