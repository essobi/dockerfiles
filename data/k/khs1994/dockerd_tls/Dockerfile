FROM alpine  
  
RUN apk add --no-cache curl \  
&& curl -L https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 > /usr/local/bin/cfssl
\  
# && curl -s -L -o /usr/local/bin/cfssljson
https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64 \  
&& curl -L https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64 >
/usr/local/bin/cfssljson \  
&& chmod +x /usr/local/bin/cfssl /usr/local/bin/cfssljson  
  
FROM alpine  
  
COPY \--from=0 /usr/local/bin /usr/local/bin  
  
WORKDIR /srv/cfssl  
  
VOLUME /srv/cfssl  
  
COPY docker-entrypoint.sh /  
  
CMD /docker-entrypoint.sh  

