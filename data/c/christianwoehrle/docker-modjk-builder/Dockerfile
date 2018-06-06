FROM ubuntu:14.04  
MAINTAINER Christian Woehrle  
  
  
RUN apt-get update && apt-get install -y wget gcc g++ build-essential  
  
RUN wget http://mirror.dkd.de/apache//httpd/httpd-2.4.10.tar.gz  
RUN wget http://mirrors.ae-online.de/apache/apr/apr-1.5.1.tar.gz  
RUN wget http://mirrors.ae-online.de/apache/apr/apr-util-1.5.4.tar.gz  
  
RUN tar zxvf httpd-2.4.10.tar.gz  
RUN tar zxvf apr-1.5.1.tar.gz  
RUN tar zxvf apr-util-1.5.4.tar.gz  
  
RUN mv apr-1.5.1 httpd-2.4.10/srclib/apr  
RUN mv apr-util-1.5.4 httpd-2.4.10/srclib/apr-util  
  
RUN wget
ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.36.tar.gz  
RUN tar zxvf pcre-8.36.tar.gz  
  
RUN cd pcre-8.36 && ./configure --prefix=/usr/local/pcre && make && make
install  
  
RUN cd httpd-2.4.10 && ./configure --prefix=/opt/apache24 --enable-mods-
shared=all --enable-so --with-included-apr --with-pcre=/usr/local/pcre && make
&& make install  
  
RUN wget http://mirror.serversupportforum.de/apache/tomcat/tomcat-
connectors/jk/tomcat-connectors-1.2.40-src.tar.gz  
RUN tar -zxf tomcat-connectors-1.2.40-src.tar.gz  
  
RUN cd tomcat-connectors-1.2.40-src/native && ./configure --with-
apxs=/opt/apache24/bin/apxs && make  
RUN mkdir /build_modjk  
RUN cp tomcat-connectors-1.2.40-src/native/apache-2.0/mod_jk.so /build_modjk  
  
VOLUME /build_modjk  
  
CMD ["cp", "tomcat-connectors-1.2.40-src/native/apache-2.0/mod_jk.so",
"/build_modjk" ]  

