FROM alpine:latest  
MAINTAINER swmacdonald  
  
RUN apk -U upgrade && \  
apk add --no-cache openvpn curl && \  
  
apk add bash && \  
  
curl -o /openvpn-strong.zip
https://www.privateinternetaccess.com/openvpn/openvpn-strong.zip && \  
unzip -d /etc/openvpn/ /openvpn-strong.zip && \  
  
# cleanup temporary files  
# rm -rf /tmp && \  
rm /openvpn-strong.zip && \  
rm -rf /var/cache/apk/*  
  
  
COPY openvpn.sh /usr/local/bin/openvpn.sh  
WORKDIR /etc/openvpn  
  
ENV REGION="US Seattle"  
ENTRYPOINT ["openvpn.sh"]  
#ENTRYPOINT ["/bin/bash"]  

