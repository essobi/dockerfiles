FROM alpine  
  
RUN apk add --update clamav && \  
rm -rf /var/cache/apk/* && \  
sed -i 's/^#Foreground .*$/Foreground yes/g' /etc/clamav/clamd.conf && \  
sed -i 's/^LocalSocket \/run\/clamav\/clamd.sock$/#LocalSocket
\/run\/clamav\/clamd.sock/g' /etc/clamav/clamd.conf && \  
sed -i 's/^#TCPSocket 3310$/TCPSocket 3310/g' /etc/clamav/clamd.conf && \  
sed -i 's/^#Foreground .*$/Foreground yes/g' /etc/clamav/freshclam.conf &&\  
freshclam -v && \  
mkdir -p /run/clamav/ && \  
chmod a+wrx /run/clamav/  
  
EXPOSE 3310  
  
CMD ["clamd"]  

