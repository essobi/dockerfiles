FROM alpine:3.7  
ENV GOLDFISH_VERSION=v0.9.0  
# CONFD  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.15.0/confd-0.15.0-linux-
amd64 /usr/local/bin/confd  
ADD confd /etc/confd  
  
# GOLDFISH  
ADD
https://github.com/Caiyeon/goldfish/releases/download/${GOLDFISH_VERSION}/goldfish-
linux-amd64 /usr/local/bin/goldfish  
  
RUN \  
apk --no-cache add bash ca-certificates openssl ;\  
chmod +x /usr/local/bin/goldfish /usr/local/bin/confd ;\  
mkdir -p /etc/goldfish  
  
EXPOSE 443  
# CONTAINER ENTRYPOINT  
ADD docker-entrypoint /docker-entrypoint  
ADD docker-entrypoint.d /docker-entrypoint.d  
ENTRYPOINT ["/docker-entrypoint"]  

