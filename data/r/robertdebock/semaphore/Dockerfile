FROM alpine:3.6  
ENV WAITFORIT_VERSION="v1.4.0"  
ENV SEMAPHORE_VERSION="v2.2.0"  
EXPOSE 3000  
RUN apk add --no-cache ansible git curl  
  
ADD https://github.com/ansible-
semaphore/semaphore/releases/download/$SEMAPHORE_VERSION/semaphore_linux_amd64
/usr/bin/semaphore  
ADD
https://github.com/maxcnunes/waitforit/releases/download/$WAITFORIT_VERSION/waitforit-
linux_amd64 /waitforit  
  
ADD semaphore.json /etc/semaphore.json  
ADD answers /answers  
  
RUN chmod +x /usr/bin/semaphore  
RUN chmod +x /waitforit  
  
# Wait until the host "mysql" is available on port 3306.  
CMD /waitforit -host=mysql -port=3306 -timeout=120 && /usr/bin/semaphore
-setup < /answers ; /usr/bin/semaphore -config /etc/semaphore.json  

