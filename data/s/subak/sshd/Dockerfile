FROM alpine:latest  
MAINTAINER Subak Systems <info@subak.jp>  
  
WORKDIR /root  
  
RUN apk add --update openssh && \  
ssh-keygen -A && \  
echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \  
echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config  
  
COPY sshd-entrypoint.sh /usr/local/bin/  
  
EXPOSE 22  
ENTRYPOINT ["sshd-entrypoint.sh"]  
CMD ["-D"]  

