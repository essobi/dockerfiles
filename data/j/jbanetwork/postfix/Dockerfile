FROM alpine:3.4  
RUN apk add --update --no-cache rsyslog bash postfix postfix-pcre openssl &&\  
touch /var/log/mail.output &&\  
chmod 666 /var/log/mail.output &&\  
echo "net.ipv4.conf.eth0.arp_ignore = 1" >> /etc/sysctl.conf &&\  
echo "net.ipv4.conf.eth0.arp_announce = 2" >> /etc/sysctl.conf  
  
COPY postfix /etc/postfix  
COPY setup.sh /root/setup.sh  
COPY setup_tls.sh /root/setup_tls.sh  
  
EXPOSE 25  
WORKDIR /root  
  
ENTRYPOINT /root/setup.sh  

