FROM golang:1.8  
ADD Makefile /go/Makefile  
ADD hack /go/hack  
ADD vendor /go/vendor  
  
ADD src /go/src  
  
RUN make build && \  
mv bin/linux/cli/docker-purge-images /usr/local/bin/docker-purge-images && \  
chmod a+x /usr/local/bin/docker-purge-images  
  
# Cleanup.  
RUN rm -fR /go  
  
CMD ["docker-purge-images"]  

