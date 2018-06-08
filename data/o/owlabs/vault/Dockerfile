# Docker file to run Hashicorp Vault (vaultproject.io)  
FROM cgswong/vault:0.5.1  
MAINTAINER Paul Beswick  
  
RUN mkdir /vault  
ADD config.hcl /vault/config.hcl  
ADD entrypoint.sh /vault/entrypoint.sh  
RUN chmod +x /vault/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/vault"]  
CMD ["version"]  

