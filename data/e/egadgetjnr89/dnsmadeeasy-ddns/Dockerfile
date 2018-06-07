FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y wget dnsutils  
  
ADD ./ddns.sh /ddns.sh  
  
RUN chmod 755 /ddns.sh  
  
# NO_HTTP_PROXY  
CMD ["/ddns.sh"]  

