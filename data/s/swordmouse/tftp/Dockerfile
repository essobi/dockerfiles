FROM alpine:latest  
  
MAINTAINER Xi Liu <swordmouse@163.com>  
  
RUN apk add --no-cache tftp-hpa \  
&& apk add --no-cache sysklogd \  
&& apk add --no-cache bash \  
&& mkdir -p /data/tftproot/ \  
&& chmod 777 /data/tftproot/  
  
VOLUME ["/data/tftproot/"]  
  
EXPOSE 69/udp  
  
ADD run.sh /run.sh  
  
RUN chmod +x /*.sh  
  
CMD ["/run.sh"]

