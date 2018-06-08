FROM alpine:3.7  
LABEL maintainer="gmblar+github@gmail.com"  
  
COPY content /  
RUN pagespeed-setup  
  
ENTRYPOINT ["pagespeed-entrypoint"]  
CMD ["collectd", "-f", "-T"]  

