FROM alpine:latest  
MAINTAINER KAMO Yasuhiro <duck1218+github@gmail.com>  
  
RUN apk --no-cache add clamav clamav-libunrar \  
&& mkdir /run/clamav \  
&& chown clamav:clamav /run/clamav  
  
RUN sed -i 's/^#Foreground .*$/Foreground true/g' /etc/clamav/clamd.conf \  
&& sed -i 's/^#TCPSocket .*$/TCPSocket 3310/g' /etc/clamav/clamd.conf \  
&& sed -i 's/^#Foreground .*$/Foreground true/g' /etc/clamav/freshclam.conf  
  
COPY entrypoint.sh /usr/bin/  
  
EXPOSE 3310  
RUN freshclam --quiet  
  
ENTRYPOINT [ "entrypoint.sh" ]  

