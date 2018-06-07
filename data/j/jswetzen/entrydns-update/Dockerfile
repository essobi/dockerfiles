FROM alpine:3.6  
MAINTAINER Johan Swetzén <johan@swetzen.com>  
  
RUN apk add --no-cache curl  
  
ADD update_entrydns.sh /etc/periodic/hourly/update_entrydns  
  
CMD /etc/periodic/hourly/update_entrydns && crond -f  

