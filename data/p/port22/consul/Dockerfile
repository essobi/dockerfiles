FROM alpine:latest  
RUN apk -U add curl wget unzip grep  
  
RUN mkdir -p /consul/config /consul/data  
RUN echo
'{"acl_datacenter":"dc1","acl_default_policy":"allow","acl_down_policy":"allow"}'
> /consul/config/master.json  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 8500 8301 8302  

