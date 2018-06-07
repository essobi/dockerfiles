FROM alpine:3.2  
ENV REFRESHED_AT 2016-05-03  
ENV VAULT_VERSION 0.5.2  
ENV VAULT_SHA256
7517b21d2c709e661914fbae1f6bf3622d9347b0fe9fc3334d78a01d1e1b4ec2  
  
ADD vault.zip /tmp/vault.zip  
RUN echo "${VAULT_SHA256} */tmp/vault.zip" | sha256sum -c - \  
&& cd /bin && unzip /tmp/vault.zip && chmod +x /bin/vault && rm /tmp/vault.zip
\  
&& apk --update add openssl ca-certificates  
  
ADD files /  
EXPOSE 8200  
ENV VAULT_ADDR "http://127.0.0.1:8200"  
ENTRYPOINT ["/bin/sh", "/start.sh"]  

