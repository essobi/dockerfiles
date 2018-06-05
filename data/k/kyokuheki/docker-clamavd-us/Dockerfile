FROM alpine  
  
LABEL maintainer Kyokuheki <kyokuheki@gmail.com>  
  
RUN apk add --update --no-cache clamav clamav-daemon clamav-libunrar freshclam  
ADD *.conf /etc/clamav/  
RUN freshclam  
  
EXPOSE 8080  
CMD freshclam & clamd  

