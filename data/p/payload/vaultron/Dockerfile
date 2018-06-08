FROM vault:latest  
  
MAINTAINER Amin Shah Gilani <gilani@payload.tech>  
  
COPY vaultConfig.json /vault/config  
  
ENTRYPOINT vault server -config=/vault/config/vaultConfig.json && \  
vault audit-enable file path=/vault/logs  

