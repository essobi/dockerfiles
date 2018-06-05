FROM scratch  
MAINTAINER ccondit@randomcoder.com  
ADD stage3.tar.xz /  
  
ENV PATH /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin  
  
RUN \  
opkg update && \  
opkg install libcurl && \  
opkg remove libcurl-bootstrap && \  
opkg upgrade && \  
opkg clean  
  
CMD ["/bin/sh"]  

