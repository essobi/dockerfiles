# FROM alpine:latest  
FROM alpine:3.3  
RUN adduser -D ircd -s /bin/false ircd  
WORKDIR /home/ircd  
  
RUN apk --update add \  
ca-certificates libgcc libstdc++ libssl1.0 libcrypto1.0 gcc libc-dev make
openssl-dev tar wget \  
&& wget https://github.com/ircd-hybrid/ircd-hybrid/archive/8.2.22.tar.gz \  
&& tar xf *.tar.gz \  
&& rm *.tar.gz \  
&& cd ircd-hybrid* \  
&& ./configure --prefix /home/ircd/ ; cat config.log \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf ircd-hybrid* \  
&& apk del gcc libc-dev openssl-dev make \  
&& rm -rf /var/cache/apk/* \  
&& chown -R ircd:ircd *  
  
USER ircd  
  
EXPOSE 6665 6666 6667 6668 6669 6697  
CMD ["/home/ircd/bin/ircd","-foreground"]  

