FROM alpine:latest  
  
# install deps  
RUN apk add --no-cache \  
curl jq bash  
  
# install our script  
COPY ddns /etc/periodic/hourly/ddns  
RUN chmod +x /etc/periodic/hourly/ddns  
  
# run once then start the cron job  
CMD /etc/periodic/hourly/ddns && crond -l 2 -f  

