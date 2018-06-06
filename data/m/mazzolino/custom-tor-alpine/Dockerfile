FROM alpine:edge  
  
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' \  
>> /etc/apk/repositories && \  
apk --update --no-cache add tor@testing su-exec  
  
COPY torrc /etc/tor/torrc  
COPY /docker-entrypoint /  
  
VOLUME /var/lib/tor  
ENTRYPOINT ["/docker-entrypoint"]  
CMD ["/usr/bin/tor"]  
EXPOSE 9050  

