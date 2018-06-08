FROM zzim2x/stellar-core-prebuilt:9.2.0-13d55680  
  
RUN apt install -y curl postgresql-client  
WORKDIR /opt/stellar-core  
  
RUN curl -O -L
https://github.com/kelseyhightower/confd/releases/download/v0.15.0/confd-0.15.0-linux-
amd64  
RUN mv confd-0.15.0-linux-amd64 /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
ENV PEER_PORT 11625  
ENV HTTP_PORT 11626  
ENV MAX_PEER_CONNECTIONS 10240  
ENV POSTGRES_DBNAME "stellar"  
ENV POSTGRES_USERNAME "postgres"  
ENV POSTGRES_UNIX_SOCKET "/var/run/posgres"  
ENV NETWORK_PASSPHRASE "Public Brave Stellar Network ; April 2018"  
ADD confd /etc/confd  
ADD entrypoint entrypoint  
  
ENTRYPOINT [ "/opt/stellar-core/entrypoint" ]  

