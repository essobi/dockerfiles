FROM alpine:latest  
LABEL maintainer Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
RUN apk --update add tor  
  
COPY torrc /etc/tor/torrc.in  
COPY run-tor.sh /usr/bin/run-tor.sh  
  
RUN chmod a+x /usr/bin/run-tor.sh  
RUN chown -R tor /etc/tor  
  
USER tor  
VOLUME ["/etc/tor/conf.d", "/var/lib/tor"]  
EXPOSE 9050/tcp 9053/tcp  
ENTRYPOINT ["/usr/bin/run-tor.sh"]  

