FROM alpine:latest  
MAINTAINER Derek Brown <derek@allderek.com>  
  
COPY files/entry.sh entry.sh  
COPY files/sshd_banner /etc/ssh/sshd_banner  
COPY files/motd /etc/motd  
COPY files/install.sh /root/install.sh  
  
RUN ./root/install.sh && \  
rm /root/install.sh  
  
EXPOSE 22  
ENTRYPOINT ["/entry.sh"]  

