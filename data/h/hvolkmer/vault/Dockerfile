FROM gliderlabs/alpine:3.1  
MAINTAINER Stephane Jourdan <fasten@fastmail.fm>  
ENV REFRESHED_AT 2015-05-05  
ENV VAULT_VERSION 0.1.2  
ADD
https://dl.bintray.com/mitchellh/vault/vault_${VAULT_VERSION}_linux_amd64.zip
/tmp/vault.zip  
RUN cd /bin && unzip /tmp/vault.zip && chmod +x /bin/vault && rm
/tmp/vault.zip  
  
RUN apk --update add curl  
  
# Include consul based default config  
# Can be overriden by volume  
RUN mkdir /config  
COPY config/consul.hcl /config/consul.hcl  
  
# Add consul register for optional consul registration  
# Start with: --entrypoint /register-run.sh  
ADD register-run.sh /register-run.sh  
RUN chmod +x /register-run.sh  
  
EXPOSE 8200  
ENV VAULT_ADDR "http://127.0.0.1:8200"  
ENTRYPOINT ["/bin/vault", "server"]  
CMD ["-dev"]  

