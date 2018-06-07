FROM alpine  
  
ENV CONSUL_CLI_VER=0.3.1  
RUN apk add --no-cache openssl && \  
wget https://github.com/CiscoCloud/consul-
cli/releases/download/v${CONSUL_CLI_VER}/consul-
cli_${CONSUL_CLI_VER}_linux_amd64.tar.gz && \  
tar zxf consul-cli_${CONSUL_CLI_VER}_linux_amd64.tar.gz && \  
mv consul-cli_${CONSUL_CLI_VER}_linux_amd64/consul-cli /usr/local/bin/ && \  
rm -rf consul-cli*  
  
CMD sh  

