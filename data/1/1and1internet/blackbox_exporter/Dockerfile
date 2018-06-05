FROM prom/blackbox-exporter:latest  
  
MAINTAINER James Eckersall <james.eckersall@gmail.com>  
  
ADD 1und1PUKIIssuingCA1-chain.pem /tmp/1und1.pem  
RUN \  
cp /etc/ssl/certs/ca-certificates.crt /tmp/ && \  
cat /tmp/ca-certificates.crt /tmp/1und1.pem> /etc/ssl/certs/ca-
certificates.crt && \  
rm /tmp/ca-certificates.crt /tmp/1und1.pem  

