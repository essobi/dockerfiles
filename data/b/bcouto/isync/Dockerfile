FROM alpine  
  
MAINTAINER bcouto@gmail.com  
  
RUN apk upgrade --no-cache  
RUN apk add --no-cache ca-certificates wget gcc make libc-dev zlib-dev \  
openssl-dev cyrus-sasl-dev db-dev  
  
RUN wget
http://netix.dl.sourceforge.net/project/isync/isync/1.2.1/isync-1.2.1.tar.gz  
  
RUN tar xvfz isync-1.2.1.tar.gz  
  
WORKDIR /isync-1.2.1  
  
RUN ./configure && make && make install  
  
WORKDIR /  
  
RUN rm -rf /isync-1.2.1 /isync-1.2.1.tar.gz  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod -v +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/usr/sbin/crond", "-f"]  

