FROM alpine:3.4  
MAINTAINER Kalle R. Møller <docker@k-moeller.dk>  
  
RUN apk add --no-cache poppler-utils  
  
ENTRYPOINT ["/usr/bin/pdftotext"]  
  
CMD ["-layout", "-", "-"]  

