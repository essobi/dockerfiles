FROM alpine:latest  
  
RUN apk add --no-cache bash util-linux openssl jq  
RUN wget
https://raw.githubusercontent.com/containous/traefik/master/contrib/scripts/dumpcerts.sh
&& \  
chmod +x dumpcerts.sh  
  
CMD ["./dumpcerts.sh", "/in/acme.json", "/out/"]  

