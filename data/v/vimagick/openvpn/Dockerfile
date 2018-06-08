#  
# Dockerfile for openvpn  
#  
FROM alpine:3.4  
MAINTAINER kev <noreply@easypi.info>  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community/" >>
/etc/apk/repositories && \  
echo "http://dl-4.alpinelinux.org/alpine/edge/testing/" >>
/etc/apk/repositories && \  
apk add --update openvpn iptables bash easy-rsa openvpn-auth-pam google-
authenticator pamtester && \  
ln -s /usr/share/easy-rsa/easyrsa /usr/local/bin && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/*  
  
ENV OPENVPN /etc/openvpn  
ENV EASYRSA /usr/share/easy-rsa  
ENV EASYRSA_PKI $OPENVPN/pki  
ENV EASYRSA_VARS_FILE $OPENVPN/vars  
  
VOLUME ["/etc/openvpn"]  
  
EXPOSE 1194/tcp 1194/udp  
  
CMD ["ovpn_run"]  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
ADD ./otp/openvpn /etc/pam.d/  

