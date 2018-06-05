FROM alpine:latest  
  
ENV CONSUL_VERSION "0.6.4"  
RUN apk update && \  
apk add wget unzip  
  
RUN wget -nv
"https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip"
\--no-check-certificate && \  
unzip consul_${CONSUL_VERSION}_linux_amd64.zip && \  
mv consul /usr/local/bin && \  
rm -f consul_${CONSUL_VERSION}_linux_amd64.zip  
  
RUN apk del wget unzip  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  

