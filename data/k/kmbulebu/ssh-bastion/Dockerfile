FROM alpine:edge  
  
RUN apk add --update \  
openssh \  
dumb-init  
  
COPY sshd_config /etc/ssh/sshd_config  
  
RUN adduser -D -s /sbin/nologin bastion  
RUN passwd -u -d bastion  
  
ONBUILD RUN ssh-keygen -A  
  
RUN mkdir /home/bastion/.ssh/  
RUN chown -R bastion:bastion /home/bastion/.ssh  
RUN chmod -R 0700 /home/bastion/.ssh  
RUN touch /home/bastion/.ssh/authorized_keys  
RUN chmod 0640 /home/bastion/.ssh/authorized_keys  
  
# Container hardening  
# Remove suid  
RUN find / -perm +6000 -type f -exec chmod a-s {} \; || true  
  
EXPOSE 2200  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
  
CMD ["/usr/sbin/sshd", "-D", "-e"]  

