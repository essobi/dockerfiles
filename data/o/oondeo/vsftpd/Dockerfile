FROM alpine  
  
# Step 1: sshd needs /var/run/sshd/ to run  
# Step 2: Remove keys, they will be generated later by entrypoint  
# (unique keys for each container)  
RUN apk add --no-cache --update vsftpd bash && \  
rm -f /etc/vsftpd/* && touch /etc/vsftpd.banned_emails  
  
ENV CHROOT="yes" PORTS="60000:60010" ADDRESS=""  
EXPOSE 20 21 60000-65535  
ADD entrypoint /usr/local/sbin/entrypoint  
ADD sshconfig /usr/local/sbin/sshconfig  
ADD vsftpd.conf /etc/  
  
VOLUME /etc/vsftpd  
  
ENTRYPOINT ["/usr/local/sbin/entrypoint"]  
  

