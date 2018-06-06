FROM alpine:3.3  
RUN adduser -S curator  
  
RUN apk add --update \  
ca-certificates \  
python \  
py-pip \  
&& pip install elasticsearch-curator \  
&& apk del py-pip \  
&& rm -rf /var/cache/apk/*  
  
USER curator  
  
ENTRYPOINT [ "/usr/bin/curator", "--certificate", "/etc/ssl/certs/ca-
certificates.crt" ]  

