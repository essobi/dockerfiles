FROM alpine  
MAINTAINER Frédéric T <xmedias@easycom.digital>  
  
# =========================================  
# Update apt-cache and install pound  
# =========================================  
RUN apk add --update --no-cache pound && rm -rf /var/cache/apl/*  
RUN deluser xfs; addgroup -g 33 -S www-data; adduser -u 33 -DSHG www-data www-
data  
  
## ================================  
## LAUNCH PART  
## ================================  
ADD poundd /usr/local/bin/  
RUN chmod +x /usr/local/bin/poundd  
  
Expose 8080 443  
VOLUME ["/pound-config"]  
  
CMD ["poundd"]

