FROM alpine:3.2  
RUN apk --update add python py-pip bash && \  
pip install s4cmd && \  
rm -fr /var/cache/apk/*  
  
RUN chmod +x /usr/bin/s4cmd  
  
WORKDIR /var/www/appliance  
  
ENTRYPOINT ["/usr/bin/s4cmd"]  
  
CMD ["--help"]  

