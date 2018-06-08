FROM alpine:latest  
MAINTAINER lars.lawoko@gmail.com  
RUN apk add --update openssh  
RUN ssh-keygen -A  
EXPOSE 22  
ENTRYPOINT ["/usr/sbin/sshd"]

