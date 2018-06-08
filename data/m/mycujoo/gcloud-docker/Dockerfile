FROM sbani/google-gloud-sdk:latest  
  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk update && \  
apk add jq docker tar consul-template@testing nodejs bash openssl postgresql
mariadb-client git py-pip  
  
RUN pip install docker-compose  
  
ADD https://releases.hashicorp.com/vault/0.9.0/vault_0.9.0_linux_amd64.zip
/tmp  
  
WORKDIR /tmp  
RUN unzip vault_0.9.0_linux_amd64.zip && mv vault /usr/local/bin  
RUN chmod +x /usr/local/bin/vault  
  
# Install HELM  
RUN bash -c "$(curl -sS
https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get)"  

