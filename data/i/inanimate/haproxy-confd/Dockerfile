FROM haproxy  
  
ENV VERSION 0.6.3  
ADD
https://github.com/kelseyhightower/confd/releases/download/v${VERSION}/confd-${VERSION}-linux-
amd64 \  
/usr/local/bin/confd  
RUN chmod u+x /usr/local/bin/confd  
  
ADD configuration.toml /etc/confd/conf.d/configuration.toml  
ADD haproxy.cfg /etc/confd/templates/haproxy.cfg  
  
ENTRYPOINT ["confd"]  

