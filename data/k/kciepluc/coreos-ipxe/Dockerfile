FROM alpine:latest  
RUN apk add --no-cache dnsmasq wget gnupg  
RUN mkdir -m 755 -p /var/lib/tftp  
ADD https://coreos.com/security/image-signing-key/CoreOS_Image_Signing_Key.asc
/tmp/CoreOS_Image_Signing_Key.asc  
RUN gpg --import /tmp/CoreOS_Image_Signing_Key.asc  
COPY coreos.ipxe /var/lib/tftp/coreos.ipxe  
COPY dnsmasq.conf /etc/dnsmasq.conf  
COPY run.sh /run.sh  
ENTRYPOINT ["/run.sh"]  
  

