FROM alpine  
RUN apk add --update perl perl-net-dns  
ADD http://www.jetmore.org/john/code/swaks/files/swaks-20170101.0/swaks swaks  
ENTRYPOINT ["/usr/bin/perl", "swaks"]  

