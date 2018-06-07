FROM alpine:3.6  
RUN apk add --no-cache openssh-server tor s6  
RUN echo PermitRootLogin yes >> /etc/ssh/sshd_config  
  
COPY entry.sh /entry.sh  
COPY torrc.tpl /etc/tor/torrc.tpl  
  
ENV TOR_PORT 9999  
ENTRYPOINT ["/entry.sh"]  
  
CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]

