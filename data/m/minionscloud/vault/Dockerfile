#  
# Vault in a Docker Container  
#  
FROM alpine:3.3  
MAINTAINER Jean-Marc Lagacé <jean-marc@m2i3.com>  
ADD https://releases.hashicorp.com/vault/0.5.2/vault_0.5.2_linux_amd64.zip
/tmp/  
RUN unzip /tmp/vault_0.5.2_linux_amd64.zip -d /usr/bin  
EXPOSE 8200  
VOLUME /config  
CMD ["/usr/bin/vault","server","-dev","-dev-listen-address=0.0.0.0:8200"]

