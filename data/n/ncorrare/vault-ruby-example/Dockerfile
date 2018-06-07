FROM ruby:2.1-onbuild  
RUN apt-get update && apt-get install -y curl unzip  
RUN curl -o /tmp/vault.zip
https://releases.hashicorp.com/vault/0.8.1/vault_0.8.1_linux_amd64.zip  
RUN curl -o /bin/tini
https://github.com/krallin/tini/releases/download/v0.16.1/tini-static-amd64  
RUN unzip /tmp/vault.zip -d /bin  
RUN chmod +x /bin/vault  
RUN chmod +x /bin/tini  
RUN chmod +x /usr/src/app/start.sh  
EXPOSE 4567/tcp  
ENTRYPOINT ["/usr/src/app/start.sh"]  

