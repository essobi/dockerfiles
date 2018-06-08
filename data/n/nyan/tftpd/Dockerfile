# Docker-tftpd  
FROM centos:latest  
  
MAINTAINER Kyle Hunter nyan@furs.community  
  
# Build container  
# docker build -t nyan/tftpd .  
# Start the container with the follonwing command:  
# docker run -it --rm -p 69:69 -v $(pwd):/tftpboot --name tftpd nyan/tftpd  
RUN adduser tftpd  
RUN mkdir /tftproot  
RUN chown tftpd:tftpd /tftproot  
  
RUN yum update -y  
RUN yum install -y tftp-server  
VOLUME /tftproot  
  
EXPOSE 69  
CMD /usr/sbin/in.tftpd --foreground --user tftpd --address 0.0.0.0:69 --secure
/tftproot

