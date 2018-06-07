FROM alpine:latest  
  
MAINTAINER Gareth Munro  
  
RUN apk update && \  
apk add bash openssh rsync && \  
mkdir -p ~root/.ssh && chmod 700 ~root/.ssh/ && \  
echo -e "Port 22\n" >> /etc/ssh/sshd_config && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 22  
RUN echo "PasswordAuthentication no" >> /etc/ssh/sshd_config  
  
COPY entry.sh /entry.sh  
  
ENTRYPOINT ["/entry.sh"]  
  
CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]  

