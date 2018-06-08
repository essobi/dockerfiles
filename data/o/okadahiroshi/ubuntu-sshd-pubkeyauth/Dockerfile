FROM ubuntu:16.04  
MAINTAINER HiroshiOkada <okadahiroshi@miobox.jp>  
  
RUN mkdir -p /var/run/sshd && \  
apt-get update && \  
apt-get install -y openssh-server openjdk-8-jre-headless  
  
RUN sed -i \  
-e "s|RSAAuthentication yes|RSAAuthentication no|" \  
-e "s|#PasswordAuthentication yes|PasswordAuthentication no|" \  
/etc/ssh/sshd_config  
  
COPY run_sshd.sh /run_sshd.sh  
  
RUN chmod +x /run_sshd.sh  
  
CMD ["/run_sshd.sh", "-e"]  
  

