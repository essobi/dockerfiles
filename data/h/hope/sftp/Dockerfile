FROM hope/base-alpine:3.4  
MAINTAINER Sergey Sadovoi <sergey@hope.ua>  
  
ENV \  
OPENSSH_VERSION=7.2 \  
SFTP_PASS=hope  
  
COPY container-files/run.sh /run.sh  
  
RUN \  
# Install  
apk add \--no-cache openssh openssh-sftp-server && \  
  
# Entrypoint  
chmod +x /run.sh  
  
COPY container-files/sshd_config /etc/ssh/sshd_config  
  
EXPOSE 22  
ENTRYPOINT ["/run.sh"]  

