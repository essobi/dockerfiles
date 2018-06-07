FROM alpine:3.4  
RUN apk --update add python py-pip && \  
pip install elasticsearch-curator==4.0.3 && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/curator"]  
  
CMD ["--help"]  

