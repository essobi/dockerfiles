FROM alpine:latest  
  
MAINTAINER Kyle Ondy <kyle@ondy.me>  
  
RUN apk add --no-cache bash openssh rsync  
RUN mkdir -p ~root/.ssh && chmod 700 ~root/.ssh/  
  
EXPOSE 22  
COPY entrypoint /entrypoint  
  
ENTRYPOINT ["/entrypoint"]  
  
CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]  

