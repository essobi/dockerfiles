FROM alpine:3.6  
MAINTAINER ilanyu <lanyu19950316@gmail.com>  
  
COPY lantern_linux_amd64 /usr/local/bin/lantern_linux_amd64  
  
RUN chmod a+x /usr/local/bin/lantern_linux_amd64  
  
EXPOSE 8787 8788  
CMD ["lantern_linux_amd64", "-proxyall"]  

