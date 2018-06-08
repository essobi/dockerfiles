FROM alpine:latest  
  
RUN apk add \--no-cache iptables ppp pptpd  
RUN echo 'option /etc/ppp/pptpd-options' > /etc/pptpd.conf && \  
echo 'pidfile /var/run/pptpd.pid' >> /etc/pptpd.conf && \  
echo 'localip 192.168.127.1' >> /etc/pptpd.conf && \  
echo 'remoteip 192.168.127.100-199' >> /etc/pptpd.conf && \  
echo 'name pptpd' > /etc/ppp/pptpd-options && \  
echo 'refuse-pap' >> /etc/ppp/pptpd-options && \  
echo 'refuse-chap' >> /etc/ppp/pptpd-options && \  
echo 'refuse-mschap' >> /etc/ppp/pptpd-options && \  
echo 'require-mschap-v2' >> /etc/ppp/pptpd-options && \  
echo 'require-mppe-128' >> /etc/ppp/pptpd-options && \  
echo 'proxyarp' >> /etc/ppp/pptpd-options && \  
echo 'nodefaultroute' >> /etc/ppp/pptpd-options && \  
echo 'lock' >> /etc/ppp/pptpd-options && \  
echo 'nobsdcomp' >> /etc/ppp/pptpd-options && \  
echo 'novj' >> /etc/ppp/pptpd-options && \  
echo 'novjccomp' >> /etc/ppp/pptpd-options && \  
echo 'nologfd' >> /etc/ppp/pptpd-options && \  
echo 'ms-dns 8.8.8.8' >> /etc/ppp/pptpd-options && \  
echo 'ms-dns 1.1.1.1' >> /etc/ppp/pptpd-options  
  
ENV PPTP_USERNAME=username \  
PPTP_PASSWORD=password  
  
EXPOSE 1723/tcp  
  
CMD set -ex && \  
echo "$PPTP_USERNAME * $PPTP_PASSWORD *" > /etc/ppp/chap-secrets && \  
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE && \  
pptpd && \  
syslogd -n -O /dev/stdout

