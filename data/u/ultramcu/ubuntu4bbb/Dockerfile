FROM ubuntu:14.04  
## Set environment variable  
ENV DEBIAN_FRONTEND noninteractive  
  
## Install required development packages  
RUN apt-get update  
RUN apt-get install -y git lzma bc gcc make libc-dev libncurses5-dev xinetd
tftpd tftp  
  
RUN touch /etc/xinetd.d/tftp  
  
RUN echo "service tftp" >> /etc/xinetd.d/tftp  
RUN echo "{" >> /etc/xinetd.d/tftp  
RUN echo "protocol = udp" >> /etc/xinetd.d/tftp  
RUN echo "port = 69" >> /etc/xinetd.d/tftp  
RUN echo "socket_type = dgram" >> /etc/xinetd.d/tftp  
RUN echo "wait = yes" >> /etc/xinetd.d/tftp  
RUN echo "user = nobody" >> /etc/xinetd.d/tftp  
RUN echo "server = /usr/sbin/in.tftpd" >> /etc/xinetd.d/tftp  
RUN echo "server_args = /tftpboot" >> /etc/xinetd.d/tftp  
RUN echo "disable = no" >> /etc/xinetd.d/tftp  
RUN echo "}" >> /etc/xinetd.d/tftp  
  
RUN mkdir /tftpboot  
RUN chmod -R 777 /tftpboot  
RUN chown -R nobody /tftpboot  
  
RUN service xinetd restart  
RUN service xinetd start  
  
RUN mv /bin/sh /bin/sh2 && ln -s /bin/bash /bin/sh  

