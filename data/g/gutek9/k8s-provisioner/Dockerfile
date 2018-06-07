FROM alpine:3.6  
RUN apk update \  
&& apk add bash curl vim jq parallel git ca-certificates --no-install-
recommends  
  
COPY provisioners provisioners  
RUN chmod -R +x provisioners  
  
CMD ["bash", "-c", "/provisioners/provisioner.sh"]  

