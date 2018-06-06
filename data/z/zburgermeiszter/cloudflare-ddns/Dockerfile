FROM alpine:3.4  
RUN apk add --update --no-cache curl jq drill  
  
ADD update-ip.sh /  
  
RUN chmod +x /update-ip.sh  
  
ENTRYPOINT ["./update-ip.sh"]

