FROM alpine:3.4  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 /confd  
RUN chmod +x /confd  
  
ADD https://github.com/cloudnautique/giddyup/releases/download/v0.14.0/giddyup
/giddyup  
RUN chmod +x /giddyup  
  
RUN apk add --update --no-cache bash curl jq  
  
ADD ./run.sh ./start_galera.sh /  
  
# Confd  
ADD ./conf.d /etc/confd/conf.d  
ADD ./templates /etc/confd/templates  
  
ENTRYPOINT ["/run.sh"]  

