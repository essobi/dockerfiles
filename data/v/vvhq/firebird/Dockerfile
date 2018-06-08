FROM ubuntu:xenial  
  
LABEL maintainer="Vladimir Bykovskiy <vladimir@vvhq.io>"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV FIREBIRD_VERSION=3.0  
ENV FIREBIRD_ARCHITECTURE=SuperClassic  
  
COPY install.sh ./install.sh  
COPY masterkey.sh ./masterkey.sh  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
  
RUN chmod +x ./install.sh && \  
sync && \  
./install.sh && \  
rm -f ./install.sh  
  
RUN chmod +x ./masterkey.sh && \  
sync && \  
./masterkey.sh && \  
rm -f ./masterkey.sh  
  
RUN chmod +x /usr/bin/entrypoint.sh && \  
sync  
  
VOLUME /var/lib/firebird/${FIREBIRD_VERSION}/data  
VOLUME /var/lib/firebird/${FIREBIRD_VERSION}/backup  
VOLUME /var/log/firebird  
  
EXPOSE 3050  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  

