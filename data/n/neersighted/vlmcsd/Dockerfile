FROM alpine:3.5  
MAINTAINER Bjorn Neergaard <bjorn@neersighted.com>  
  
RUN apk add --no-cache --virtual .deps curl g++ make \  
&& curl -SL https://github.com/Wind4/vlmcsd/archive/master.tar.gz \  
| tar -xz -C / \  
&& make -C /vlmcsd-master \  
&& apk del .deps  
  
ENV PATH /vlmcsd-master/bin:$PATH  
EXPOSE 1688  
ENTRYPOINT ["vlmcsd", "-D", "-e", "-j", "/vlmcsd-master/etc/vlmcsd.kmd"]  

