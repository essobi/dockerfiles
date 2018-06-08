FROM alpine:3.5  
LABEL maintainer "Matthieu Buffet <mtth.bfft@gmail.com>"  
  
RUN apk add --no-cache \  
quassel-core \  
icu-libs \  
qt-sqlite \  
openssl  
  
RUN mkdir /etc/quasselcore/ && \  
chown -R quassel:root /etc/quasselcore/  
  
WORKDIR /etc/quasselcore/  
  
# Default to prevent running as root if no --user or user namespace set up  
USER quassel  
  
VOLUME ["/etc/quasselcore/"]  
  
ENTRYPOINT ["/usr/bin/quasselwrapper.sh"]  
CMD ["-c","/etc/quasselcore/","--require-ssl"]  
  
EXPOSE 4242  
COPY openssl.cnf /etc/quasselcore/  
COPY gen_certificate.sh /etc/quasselcore/  
COPY wrapper.sh /usr/bin/quasselwrapper.sh  

