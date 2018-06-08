FROM alpine:edge  
  
EXPOSE 8118 9050 9151  
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' \  
>> /etc/apk/repositories && \  
apk --update add privoxy tor@testing runit@testing  
  
RUN echo "SocksPort 9050" >> /etc/tor/torrc  
RUN echo "ControlPort 9151" >> /etc/tor/torrc  
RUN echo "CookieAuthentication 1" >> /etc/tor/torrc  
RUN echo "forward-socks5 / localhost:9050 ." >> /etc/privoxy/config  
  
COPY service /etc/service/  
  
CMD ["runsvdir", "/etc/service"]  

