FROM sickp/alpine-sshd:latest  
ADD https://github.com/erikthorselius.keys /home/regius/.ssh/authorized_keys  
RUN \  
passwd -d root && \  
adduser -D -s /bin/ash regius && \  
passwd -u regius && \  
chown -R regius:regius /home/regius  

