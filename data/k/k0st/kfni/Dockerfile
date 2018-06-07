FROM gliderlabs/alpine  
MAINTAINER kost - https://github.com/kost  
  
RUN apk --update add openssl && rm -f /var/cache/apk/* && \  
wget https://github.com/kost/libsimplebloom/raw/master/bin/bloomutil-
static-i586 -O /usr/local/bin/bloomutil && chmod 755 /usr/local/bin/bloomutil  
# RUN wget https://github.com/kost/libsimplebloom/raw/master/bin/bloomutil-
static-x64 -O /usr/local/bin/bloomutil && chmod 755 /usr/local/bin/bloomutil  
ADD /scripts /bloom/  
RUN adduser -D -s /bin/sh user user && chown -R user /bloom && chmod 755
/bloom/* && mkdir /work && chown user /work  
  
USER user  
RUN /bloom/preparedb.sh  
  
VOLUME /work  
WORKDIR /work  
  
ENTRYPOINT ["bloomutil"]  
  
CMD ["-h"]  

