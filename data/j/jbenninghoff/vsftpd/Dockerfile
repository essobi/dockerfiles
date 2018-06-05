FROM alpine  
RUN apk add --no-cache vsftpd tzdata  
RUN echo "seccomp_sandbox=NO" >> /etc/vsftpd/vsftpd.conf  
  
VOLUME /var/lib/ftp  
EXPOSE 21  
CMD ["vsftpd", "/etc/vsftpd/vsftpd.conf"]  

