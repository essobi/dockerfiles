FROM alpine:latest  
MAINTAINER mamemomonga  
  
RUN set -xe && \  
apk update && \  
apk add openssh  
  
RUN set -xe && \  
mkdir -p -m 0700 /root/.ssh && \  
touch /root/.ssh/authorized_keys && \  
chmod 600 /root/.ssh/authorized_keys && \  
echo 'PermitRootLogin without-password' >> /etc/ssh/sshd_config && \  
echo 'PasswordAuthentication no' >> /etc/ssh/sshd_config  
  
ADD start.sh /start.sh  
RUN chmod 700 /start.sh  
  
EXPOSE 22  
CMD /start.sh  

