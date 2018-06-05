FROM sosedoff/pgweb  
MAINTAINER Masaki Muranaka <monaka@monami-ya.com>  
  
RUN apk update && \  
update-ca-certificates && \  
apk add bash  
  
ENTRYPOINT ["/usr/bin/pgweb"]  
CMD ["--bind=0.0.0.0", "--listen=8081"]  

