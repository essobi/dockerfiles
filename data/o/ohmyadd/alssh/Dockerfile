FROM alpine  
  
COPY dist /root/dist  
RUN apk add --no-cache openssh-server && \  
rm -rf /var/cache/ && \  
rm /etc/ssh/sshd_config && \  
echo "root:root" | chpasswd && \  
mv /root/dist/sshd_config /etc/ssh/sshd_config && \  
ssh-keygen -A && \  
rm -rf /root/dist  
  
CMD /usr/sbin/sshd -D  
  

