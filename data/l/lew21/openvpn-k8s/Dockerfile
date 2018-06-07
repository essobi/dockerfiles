FROM alpine:3.5  
RUN apk --no-cache add openvpn iptables openvpn-auth-pam linux-pam ca-
certificates openssl  
  
RUN update-ca-certificates  
RUN wget https://gitlab.com/LEW21/pam-https/builds/8867127/artifacts/file/pam-
https -O /usr/local/bin/pam-https  
RUN chmod ugo+x /usr/local/bin/pam-https  
  
EXPOSE 1194/tcp  
EXPOSE 1194/udp  
  
WORKDIR /etc/openvpn  
RUN rm /etc/openvpn/*  
  
ADD run.sh /usr/local/bin/run.sh  
CMD ["/bin/sh", "/usr/local/bin/run.sh"]  

