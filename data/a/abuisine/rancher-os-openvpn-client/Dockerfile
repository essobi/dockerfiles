FROM kylemanna/openvpn  
LABEL maintainer="Alexandre Buisine <alexandrejabuisine@gmail.com>"
version="1.2.0"  
  
COPY resources/docker-entrypoint.sh /usr/local/sbin/docker-entrypoint.sh  
COPY resources/iptables.sh /usr/local/sbin/iptables.sh  
  
RUN chmod +x /usr/local/sbin/docker-entrypoint.sh /usr/local/sbin/iptables.sh  
  
ENV PASSWORD=dummy CA_URL=dummy  
  
ENTRYPOINT [ "/usr/local/sbin/docker-entrypoint.sh" ]  
#should be used with --script-security 2 --up /usr/local/sbin/iptables.sh
--auth-user-pass /tmp/auth

