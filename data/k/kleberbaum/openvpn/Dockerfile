# Original credit: https://github.com/jpetazzo/dockvpn  
FROM alpine:latest  
  
LABEL description "OpenVPN is a full-featured open-source VPN software"  
  
# this fork is maintained by kleberbaum  
MAINTAINER Florian Kleber <kleberbaum@erebos.xyz>  
  
# needed by scriptsOpenVPN  
ENV OPENVPN /etc/openvpn  
ENV EASYRSA /usr/share/easy-rsa  
ENV EASYRSA_PKI $OPENVPN/pki  
ENV EASYRSA_VARS_FILE $OPENVPN/vars  
  
# place bin  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
# add support for OTP authentication using a PAM module  
ADD ./otp/openvpn /etc/pam.d/  
  
RUN echo "## Installing base ##" && \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >>
/etc/apk/repositories && \  
echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community/" >>
/etc/apk/repositories && \  
apk upgrade --update-cache --available && \  
\  
apk add --force \  
iptables \  
bash \  
openvpn@testing \  
easy-rsa@testing \  
openvpn-auth-pam@testing \  
google-authenticator@testing \  
pamtester@testing \  
tini@community \  
\  
&& ln -s /usr/share/easy-rsa/easyrsa /usr/local/bin \  
&& rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*  
  
# internally uses port 1194/udp, remap using `docker run -p 443:1194/tcp`  
EXPOSE 1194/udp  
  
# management interface  
EXPOSE 2080/tcp  
  
VOLUME /etc/openvpn  
  
# place init script  
RUN cp -p /usr/local/bin/ovpn_run_simple /run.sh  
  
# I personaly like to start my containers with tini ^^  
ENTRYPOINT ["/sbin/tini", "--", "/run.sh"]  

