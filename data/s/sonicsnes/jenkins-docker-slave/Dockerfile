FROM docker  
  
RUN \  
apk add --update bash openssh openjdk7-jre-base git rsync && \  
rm -rf /var/cache/apk/*  
  
ADD entrypoint.sh /root/entrypoint.sh  
  
RUN \  
chmod +x /root/entrypoint.sh && \  
sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication yes/'
/etc/ssh/sshd_config && \  
sed -i 's/^#PermitUserEnvironment no/PermitUserEnvironment yes/'
/etc/ssh/sshd_config && \  
ssh-keygen -A -N ''  
  
EXPOSE 22  
ENTRYPOINT []  
CMD /root/entrypoint.sh  

