FROM alpine:latest  
LABEL maintainer="Marc Mettke <marc@itmettke.de>"  
  
RUN apk --no-cache add openssh rsync && \  
mkdir -p /config/auth /config/keys && \  
touch /config/auth/authorized_keys && \  
ssh-keygen -A && \  
mv /etc/ssh/ssh_host_* /config/keys/ && \  
cp /etc/ssh/sshd_config /config && \  
adduser -D local && \  
mkdir /home/local/.ssh && \  
ln -s /config/auth/authorized_keys /home/local/.ssh/authorized_keys && \  
chown local:local /home/local -R && \  
sed -i -e 's/local:!:/local::/g' /etc/shadow  
  
EXPOSE 22  
VOLUME /config  
  
ENTRYPOINT [ "/usr/sbin/sshd", \  
"-D", \  
"-o", \  
"HostKey=/config/keys/ssh_host_rsa_key", \  
"-o", \  
"HostKey=/config/keys/ssh_host_dsa_key", \  
"-o", \  
"HostKey=/config/keys/ssh_host_ecdsa_key", \  
"-o", \  
"HostKey=/config/keys/ssh_host_ed25519_key", \  
"-o", \  
"PermitRootLogin=no", \  
"-o", \  
"PasswordAuthentication=no" \  
]  
HEALTHCHECK CMD /bin/ash -c "PID=\$(cat /run/sshd.pid) && [ -n \"\${PID}\" -a
-d \"/proc/\${PID}\" ] && exit 0 || exit 1"  

