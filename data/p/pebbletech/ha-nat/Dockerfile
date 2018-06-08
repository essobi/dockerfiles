FROM alpine:3.2  
RUN apk add --update bash curl iptables python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm -Rf /var/cache/apk/*  
  
ADD ha-nat.sh /ha-nat.sh  
  
CMD [ "/ha-nat.sh" ]  
  

