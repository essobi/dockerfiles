FROM alpine:latest  
  
MAINTAINER Christopher 'Chief' Najewicz <chief@beefdisciple.com>  
  
ENV version=0.5.1  
ADD
https://releases.hashicorp.com/vault/${version}/vault_${version}_linux_amd64.zip
/tmp/vault.zip  
  
RUN \  
cd /bin &&\  
unzip /tmp/vault.zip &&\  
chmod +x /bin/vault &&\  
rm /tmp/vault.zip &&\  
apk update &&\  
apk add ca-certificates  
  
EXPOSE 8200  
VOLUME /etc/vault.hcl  
  
ENTRYPOINT ["/bin/vault", "server"]  
  
CMD ["-config=/etc/vault.hcl"]  

