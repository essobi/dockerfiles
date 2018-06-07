FROM fnichol/uhttpd:latest  
  
# proper init  
ADD https://github.com/krallin/tini/releases/download/v0.14.0/tini-static
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
VOLUME /www  
  
CMD ["/usr/sbin/run_uhttpd", "-f", "-p", "80", "-h", "/www"]  

