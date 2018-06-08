FROM alpine:latest  
MAINTAINER "MrWorta <mrworta@nightsky.de>"  
RUN apk update; apk upgrade  
RUN apk add tftp-hpa  
  
RUN mkdir -p /opt/tftp/download; chmod -R 777 /opt/tftp  
RUN echo Gri "^.* download/\0" > /etc/tftp.map  
  
VOLUME /opt/tftp  
  
EXPOSE 69/udp  
  
WORKDIR /opt/tftp  
ENTRYPOINT ["/usr/sbin/in.tftpd", "-t", "0", "-p", "-m", "/etc/tftp.map",
"-c", "-vvv", "-u", "root", "--secure", "--foreground", "/opt/tftp"]  

