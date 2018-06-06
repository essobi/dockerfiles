FROM alpine:3.7  
RUN apk add --no-cache clamav freshclam clamav-libunrar  
  
RUN sed -i 's/^#Foreground .*$/Foreground yes/g' /etc/clamav/clamd.conf; \  
sed -i 's/^#TCPSocket .*$/TCPSocket 3310/g' /etc/clamav/clamd.conf; \  
sed -i 's/^#MaxDirectoryRecursion .*$/MaxDirectoryRecursion 25/g'
/etc/clamav/clamd.conf; \  
sed -i 's/^#OnAccessMaxFileSize .*$/OnAccessMaxFileSize 50M/g'
/etc/clamav/clamd.conf; \  
sed -i 's/^#PCREMaxFileSize .*$/PCREMaxFileSize 50M/g' /etc/clamav/clamd.conf;
\  
sed -i 's/^#StreamMaxLength .*$/StreamMaxLength 50M/g' /etc/clamav/clamd.conf;
\  
sed -i 's/^#Foreground .*$/Foreground yes/g' /etc/clamav/freshclam.conf; \  
sed -i 's/^#Checks .*$/Checks 24/g' /etc/clamav/freshclam.conf  
  
RUN mkdir /run/clamav && chown clamav:clamav /run/clamav  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
EXPOSE 3310/tcp  
  
ENTRYPOINT ["/entrypoint.sh"]  

