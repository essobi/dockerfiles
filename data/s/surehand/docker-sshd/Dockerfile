FROM alpine:3.7  
# Add openssh  
RUN apk add --no-cache openssh-server  
  
# Copy sshd config  
RUN ssh-keygen -A  
ADD sshd_config /etc/ssh/sshd_config  
  
# Create user  
RUN adduser -D -g ",,," -h /home/ssh ssh && \  
echo "ssh:" | chpasswd && \  
mkdir -p /home/ssh/.ssh && \  
chown root:root /home/ssh && \  
chmod 755 /home/ssh  
  
EXPOSE 22  
#Adding the script which will start required processes  
ADD docker-run.sh /root/docker-run.sh  
RUN chmod +x /root/docker-run.sh  
  
CMD ["/root/docker-run.sh"]  

