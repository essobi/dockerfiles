# arch  
# VERSION 0.1  
FROM alpine  
  
MAINTAINER Justin Allen <justin@justinallen.me>  
  
RUN adduser -S ircd -h /opt/inspircd  
  
#RUN cd /tmp; curl
https://codeload.github.com/inspircd/inspircd/tar.gz/v2.0.20 | tar -zx; cd
inspircd-2.0.20; ./configure --enable-extras="m_ssl_gnutls.cpp"; ./configure
--prefix=/opt/inspircd --enable-openssl --uid ircd ; make; make install  
ADD bootstrap.sh /tmp/  
RUN chmod +x /tmp/bootstrap.sh && /tmp/bootstrap.sh  
  
ENTRYPOINT ["/opt/inspircd/start.sh"]  
  
EXPOSE 7000  
ADD scripts/* /opt/inspircd/  

