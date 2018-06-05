# Original credit: https://github.com/jpetazzo/dockvpn  
# Addition credit: https://github.com/kylemanna/docker-openvpn  
# Smallest base image  
FROM schmich/armv7hf-alpine-qemu:3.5  
#enable building ARM container on x86 machinery on the web (comment out next 3
lines if built on Raspberry)  
RUN [ "cross-build-start" ]  
  
LABEL maintainer="netpi@hilscher.com" \  
version="V0.9.1.0" \  
description="Alpine Linux with an OpenVPN server plus EasyRSA PKI CA"  
  
# Testing: pamtester  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >>
/etc/apk/repositories && \  
apk add --update openvpn iptables bash easy-rsa openvpn-auth-pam google-
authenticator pamtester lighttpd && \  
ln -s /usr/share/easy-rsa/easyrsa /usr/local/bin && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/* && \  
echo "server.port = 1194" >> /etc/lighttpd/lighttpd.conf && \  
echo "<html><body><a href="client.ovpn">Click here to download your
client.opvn key file to import into your OpenVPN client</a></body></html>" >
/var/www/localhost/htdocs/index.html  
  
# Needed by scripts  
ENV OPENVPN /etc/openvpn  
ENV EASYRSA /usr/share/easy-rsa  
ENV EASYRSA_PKI $OPENVPN/pki  
ENV EASYRSA_VARS_FILE $OPENVPN/vars  
  
# location of client configuration ovpn file for web server  
ENV CLIENT_OVPN /var/www/localhost/htdocs/client.ovpn  
  
# Prevents refused client connection because of an expired CRL  
ENV EASYRSA_CRL_DAYS 3650  
VOLUME ["/etc/openvpn"]  
  
# Internally uses port 1194/udp, remap using `docker run -p 443:1194/tcp`,
1194/tcp used for web server  
EXPOSE 1194/udp 1194/tcp  
  
# command checks if certificates are available. If not then it starts the web
server  
CMD ["sh", "-c", "[ -f /etc/openvpn/pki/crl.pem ] && ovpn_run || lighttpd -D
-f /etc/lighttpd/lighttpd.conf"]  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
# Add support for OTP authentication using a PAM module  
ADD ./otp/openvpn /etc/pam.d/  
  
#stop processing ARM emulation (comment out next line if built on Raspberry)  
RUN [ "cross-build-end" ]  

